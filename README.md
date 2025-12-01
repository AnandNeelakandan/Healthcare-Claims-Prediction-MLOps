# 🚀 ClaimPredict AI – End-to-End Medical Claim Status Prediction (MLOps)

### 🌐 Live Demo (Frontend – Framer)
👉 **https://numerous-area-128663.framer.website/**

### 🧾 API Documentation (Swagger)
👉 **https://healthcare-claims-prediction-mlops.onrender.com/docs**

### ⚡ Backend API (Render Deployment)
👉 **https://healthcare-claims-prediction-mlops.onrender.com**

---

# 🧠 Project Overview

**ClaimPredict AI** is a fully deployed **Machine Learning + MLOps system** designed to predict **medical claim status** (Paid or Denied) instantly.  
It helps hospitals and insurance teams optimize **Revenue Cycle Management (RCM)** by reducing claim denials and improving cash flow.

This end-to-end system includes:

- 🧠 **ANN Model** trained on engineered healthcare claim features  
- ⚙️ **FastAPI backend** with real-time prediction endpoint  
- 🖥️ **Modern Framer UI** for user interaction  
- ☁️ **Render Cloud Deployment**  
- 📊 **Synthetic + realistic industry-style claims dataset**  
- 🚀 **MLOps-ready directory structure**  

---

# 🖥️ System Components

## **1️⃣ Frontend — Framer Web App**
A clean, modern landing page + prediction interface.

Users can:
- Enter claim details  
- Predict Paid/Denied instantly  
- View explanations  
- Navigate through sections  

👉 Live URL:  
`https://numerous-area-128663.framer.website/`

---

## **2️⃣ Backend — FastAPI (Render Deployment)**

### API Endpoints:
- `POST /predict` → Predict claim status  
- `GET /claims/{id}` → Claim lookup  
- `GET /members/{id}` → Member lookup  
- `GET /providers/{npi}` → Provider lookup  

👉 Swagger UI:  
`https://healthcare-claims-prediction-mlops.onrender.com/docs`

👉 Base API URL:  
`https://healthcare-claims-prediction-mlops.onrender.com/`

---

# 🧠 Machine Learning Model — ANN + Feature Engineering

The system uses:
- Billed/Allowed ratio  
- Timely filing days  
- Network status  
- Policy active/inactive  
- Provider specialty  
- Age group  
- Gender  

### 🏆 Final Model Performance

| Model | Accuracy | Notes |
|-------|----------|------------------------------|
| **ANN (Final Model)** | **76.20%** | Best for complex data |
| Random Forest | 74.95% | Good generalization |
| XGBoost | 74.40% | Robust boosting |

---

# 🧪 API Usage Examples

### **📌 Prediction Endpoint**
**POST /predict**

#### Example Request:
```json
{
  "BilledAmount": 1200,
  "AllowedAmount": 850,
  "Days_to_File": 25,
  "Is_Out_Of_Network": 0,
  "Is_Policy_Active": 1,
  "PatientGender": "F",
  "ProviderSpecialty": "Radiology",
  "PatientAgeGroup": "Adult"
}
```

#### Example Response:
```json
{
  "prediction": "PAID",
  "explanation": "High allowed amount, active policy, low filing delay."
}
```

---

# 📘 Dataset

You can use the dataset to test predictions manually:

`/Datasets/final_claims_data_industry.csv`

Use any sample row to test:
- Swagger UI  
- Framer UI  
- Postman  

---

# ⚙️ Running Backend Locally

```bash
git clone https://github.com/AnandNeelakandan/Healthcare-Claims-Prediction-MLOps.git
cd Healthcare-Claims-Prediction-MLOps
pip install -r requirements.txt
uvicorn ML_API:app --reload
```

Swagger UI (local):
```
http://localhost:8000/docs
```

---

# 📁 Repository Structure

```
📦 Healthcare-Claims-Prediction-MLOps
 ┣ 📂 Datasets
 ┣ 📂 ML pipeline notebooks
 ┣ 📂 routers
 ┣ 📂 src
 ┣ 📜 ML_API.py
 ┣ 📜 requirements.txt
 ┣ 📜 ann_model.keras
 ┣ 📜 scaler.pkl
 ┣ 📜 render.yaml
 ┗ 📜 README.md
```

---

# ✨ Features

✔ Real-time ML predictions  
✔ ANN model with heavy feature engineering  
✔ FastAPI backend with multiple lookup tools  
✔ Fully deployed using Render  
✔ Framer interactive UI  
✔ MLOps-ready folder pattern  
✔ Industry-style synthetic dataset  

---

# 👤 Author: Anand Neelakandan
AI Engineer • Machine Learning • Deep Learning • MLOps  
GitHub: https://github.com/AnandNeelakandan
Linkedin: www.linkedin.com/in/anand-neelakandan-ab3219380

---

# ⭐ If this project helps you, star the repository!
