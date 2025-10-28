# 🏥 Healthcare Claims Prediction: Optimizing Revenue Cycle Management (RCM)

## Project Overview

This project implements a robust machine learning pipeline to address a critical pain point in the **US Healthcare** industry: predicting medical claim status to prevent revenue loss.

The system is designed to classify incoming claims into one of three critical statuses (**Paid, Denied, or Pending**). By accurately flagging high-risk claims (specifically **Denials**) early in the process, this solution empowers healthcare providers to optimize their **Revenue Cycle Management (RCM)**, reduce administrative costs, and improve cash flow.

---

## 🎯 Phase 1 Complete: Advanced Model Development & Benchmarking

### Key Technical Achievements:

1.  **Synthetic Data Engineering:** Overcame the challenge of proprietary data access by **designing and coding a custom Python generator** (`src/01_data_generator.py`). This script simulates **10,000 realistic claims** incorporating complex insurance logic (eligibility, timely filing limits, OON rules) crucial for training a high-fidelity model.
2.  **High-Signal Feature Engineering:** Developed powerful predictive features, notably the **Billed-to-Allowed Ratio**, which provides a consolidated, high-value signal of billing compliance to the models.
3.  **Ensemble & Deep Learning Benchmarking:** Compared three optimized classification strategies on the balanced dataset:
    * **Artificial Neural Network (ANN)**
    * **XGBoost Classifier** (Gradient Boosting)
    * **Random Forest Classifier** (Bagging Ensemble)

### Model Performance Summary:

The **Artificial Neural Network** was the strongest performer, achieving **76.20% accuracy** on the unseen test set after handling class imbalance with SMOTE.

| Model | Final Test Accuracy | Note |
| :--- | :--- | :--- |
| **Artificial Neural Network** | **76.20%** | Best Performer for complex, non-linear relationships. |
| **Random Forest** | 73.95% | Excellent generalization capability. |
| **XGBoost** | 73.40% | Highly robust boosting ensemble. |

---

## 🛣️ Roadmap: MLOps and Production Deployment

The project is architected for continuous operation via an **MLOps** pipeline.

The focus of the next phase is moving the top-performing ANN model from the notebook to a reliable production environment:

1.  **Deployment API:** Develop a **RESTful API** (using Flask/FastAPI) to serve real-time predictions to operational systems.
2.  **Containerization:** Use **Docker** to ensure the model and its dependencies are portable and stable across different environments.
3.  **Model Monitoring:** Implement a solution for **data drift and performance decay detection** to ensure the model maintains its accuracy over time with real-world claim submissions.

---

## 📁 Repository Structure

| Folder/File | Description | Location |
| :--- | :--- | :--- |
| `data/` | Contains the `final_claims_data_industry.csv` synthetic dataset. | **`data/`** |
| `src/` | Contains the core data generation script. | **`src/`** |
| `notebooks/` | Contains the full exploratory data analysis (EDA) and modeling pipeline notebook. | **`notebooks/`** |
| `README.md` | This project overview. | Root |
