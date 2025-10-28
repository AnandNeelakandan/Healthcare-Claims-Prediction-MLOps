import pandas as pd
import numpy as np
import uuid
from datetime import timedelta, date

# --- 1. SETUP ---
np.random.seed(420) # Ensures the data is the same every time you run it
N_ROWS = 10000

# --- 2. IDENTIFIER COLUMNS (Non-Predictive Noise for Realism) ---
start_date = date(2023, 1, 1)
data = pd.DataFrame({
    'ClaimID': [str(uuid.uuid4()) for _ in range(N_ROWS)],
    'MemberID': [f'M{i:05d}' for i in np.random.randint(1, N_ROWS // 2, N_ROWS)],
    'ProviderNPI': [f'P{i:04d}' for i in np.random.randint(1, 800, N_ROWS)],
    'AccountNum': np.random.randint(100000, 999999, N_ROWS),
    'TaxID': np.random.randint(10000, 99999, N_ROWS),
    'DateOfService': [(start_date + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d') for _ in range(N_ROWS)],
})

# --- 3. CORE PREDICTIVE FEATURES (The Statistical Complexity) ---
data['BilledAmount'] = np.random.uniform(500, 15000, N_ROWS)
data['Is_Out_Of_Network'] = np.random.choice([True, False], N_ROWS, p=[0.20, 0.80]) # 80% In-Network
data['AllowedAmount'] = data.apply(
    # Complex rule: OON claims get lower allowance (lower Allowed/Billed ratio)
    lambda row: row['BilledAmount'] * np.random.uniform(0.9, 0.95) if not row['Is_Out_Of_Network']
    else row['BilledAmount'] * np.random.uniform(0.5, 0.75), axis=1
)
data['Is_Policy_Active'] = np.random.choice([True, False], N_ROWS, p=[0.88, 0.12]) # Eligibility
data['Days_to_File'] = np.maximum(0, np.random.normal(25, 50, N_ROWS)).astype(int) # Timeliness

# --- 4. NOISE/REALISM FEATURES ---
data['PatientAge'] = np.random.randint(1, 90, N_ROWS)
data['PatientGender'] = np.random.choice(['M', 'F'], N_ROWS)
data['ProviderSpecialty'] = np.random.choice(['Internal Medicine', 'Cardiology', 'Physical Therapy', 'Radiology'], N_ROWS)

# --- 5. TARGET VARIABLE (ClaimStatus) with COMPLEX RULES ---
def set_claim_status_final(row):
    # Rule A: High-Confidence Deny
    if not row['Is_Policy_Active']: return 'Denied'
    if row['Days_to_File'] > 180: return 'Denied'
    if row['AllowedAmount'] / row['BilledAmount'] < 0.5: return 'Denied'

    # Rule B: High-Confidence Paid
    if (not row['Is_Out_Of_Network'] and row['Days_to_File'] < 30 and row['AllowedAmount'] / row['BilledAmount'] > 0.9):
        return np.random.choice(['Paid', 'Pending'], p=[0.9, 0.1]) # 90% chance of paid

    # Rule C: Complex/Pending Cases (The "Hidden Pattern" Area)
    if row['Is_Out_Of_Network']:
        return np.random.choice(['Pending', 'Denied'], p=[0.6, 0.4]) # OON usually Pending/Denied

    if row['Days_to_File'] > 60:
        return np.random.choice(['Pending', 'Denied'], p=[0.7, 0.3]) # Late claims are usually Pending/Denied

    # Default: Remaining active, moderately compliant claims are usually Pending or Paid
    return np.random.choice(['Pending', 'Paid'], p=[0.6, 0.4])

data['ClaimStatus'] = data.apply(set_claim_status_final, axis=1)

# --- 6. EXPORT THE FINAL 15 COLUMNS ---
FINAL_COLS = [
    'ClaimID', 'MemberID', 'ProviderNPI', 'AccountNum', 'TaxID',
    'DateOfService', 'BilledAmount', 'AllowedAmount', 'Is_Out_Of_Network',
    'Days_to_File', 'Is_Policy_Active', 'PatientAge', 'PatientGender',
    'ProviderSpecialty', 'ClaimStatus'
]
data = data[FINAL_COLS]

# Save the file in both requested formats
data.to_csv('final_claims_data_industry.csv', index=False)
data.to_excel('final_claims_data_industry.xlsx', index=False)

print("\n------------------------------------------------------------------")
print("✅ SUCCESS: The following files have been created in your Colab files tab:")
print("1. final_claims_data_industry.csv")
print("2. final_claims_data_industry.xlsx")
print("------------------------------------------------------------------")
