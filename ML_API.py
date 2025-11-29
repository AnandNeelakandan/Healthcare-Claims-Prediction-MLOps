import os

# ==========================================
#   ENVIRONMENT SETUP (Disable GPU on Render)
# ==========================================
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel
from tensorflow.keras.models import load_model

# Database Routers
from routers.claims import router as claims_router
from routers.members import router as members_router
from routers.providers import router as providers_router

# ==========================================
#               GEMINI SETUP
# ==========================================
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
explain_model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================================
#           INITIALIZE FASTAPI
# ==========================================
app = FastAPI(title="Medical Claim Prediction API with LLM Explanation")

# ==========================================
#        CORS (IMPORTANT FOR FRAMER)
# ==========================================
# Allow ALL origins including Framer hosted domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # <--- FIXED (THE MAIN PROBLEM)
    allow_credentials=True,
    allow_methods=["*"],          # Allow GET, POST, OPTIONS
    allow_headers=["*"],          # Allow all headers
)

# ==========================================
#     LOAD ANN & PREPROCESS FILES
# ==========================================
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")
numeric_columns = joblib.load("numeric_columns.pkl")
feature_columns = joblib.load("feature_columns.pkl")
model = load_model("ann_model.keras")

# ==========================================
#             INPUT MODEL
# ==========================================
class ClaimInput(BaseModel):
    BilledAmount: float
    AllowedAmount: float
    Days_to_File: float
    Is_Out_Of_Network: int
    Is_Policy_Active: int
    PatientGender: str
    ProviderSpecialty: str
    PatientAgeGroup: str

# ==========================================
#             ROOT CHECK
# ==========================================
@app.get("/")
def root():
    return {"status": "API is running"}

# ==========================================
#             HEALTH CHECK
# ==========================================
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API working fine"}

# ==========================================
#               PREDICT
# ==========================================
@app.post("/predict")
def predict_claim(data: ClaimInput):

    df = pd.DataFrame([data.dict()])

    # Derived feature
    df["BilledToAllowedRatio"] = df["BilledAmount"] / (df["AllowedAmount"] + 1)

    # Fix categories
    df["PatientGender"] = pd.Categorical(df["PatientGender"], categories=["F", "M"])
    df["ProviderSpecialty"] = pd.Categorical(
        df["ProviderSpecialty"],
        categories=["Cardiology", "Internal Medicine", "Physical Therapy", "Radiology"]
    )
    df["PatientAgeGroup"] = pd.Categorical(
        df["PatientAgeGroup"],
        categories=["child/young", "Adult", "senior", "Elderly"]
    )

    df["Is_Out_Of_Network"] = df["Is_Out_Of_Network"].astype(int)
    df["Is_Policy_Active"] = df["Is_Policy_Active"].astype(int)

    df = pd.get_dummies(df)
    df = df.reindex(columns=feature_columns, fill_value=0)

    df[numeric_columns] = scaler.transform(df[numeric_columns])

    # ANN prediction
    preds = model.predict(df)
    pred_class = np.argmax(preds)
    final_label = label_encoder.inverse_transform([pred_class])[0]

    # ======================================
    #       GEMINI EXPLANATION
    # ======================================
    explanation_prompt = f"""
A medical claim prediction model returned: {final_label}.

Explain why this claim is likely {final_label}.
If denied, list possible reasons:
- inactive policy
- out of network
- missing documents
- filing delay
- incorrect codes
- eligibility issues

If paid, explain briefly why it is valid.

Keep the explanation short and simple.
"""

    llm_response = explain_model.generate_content(explanation_prompt)
    llm_text = llm_response.text

    return {
        "prediction": final_label,
        "explanation": llm_text
    }

# ==========================================
#        INCLUDE DB ROUTERS
# ==========================================
app.include_router(claims_router)
app.include_router(members_router)
app.include_router(providers_router)
