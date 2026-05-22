# Medicare Fraud Detection Using Machine Learning

## Project Overview

Healthcare fraud is one of the major challenges in the insurance and medical industry. Fraudulent claims lead to huge financial losses and inefficient healthcare systems.

This project focuses on detecting potentially fraudulent healthcare providers using Machine Learning techniques on Medicare claim datasets.

The project includes:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Fraud Classification using Machine Learning
- Feature Importance Analysis
- Fraud Prediction on unseen test data

---

# Problem Statement

The objective of this project is to identify whether a healthcare provider is potentially fraudulent based on:
- claim reimbursement patterns,
- diagnosis codes,
- procedure codes,
- physician involvement,
- chronic conditions,
- beneficiary details.

---

# Dataset

The project uses Medicare healthcare claim datasets.

## Files Used

| File | Description |
|------|-------------|
| TRAIN1.csv | Raw healthcare claims dataset used for EDA |
| TRAIN2.csv | Feature-engineered dataset used for model training |
| TEST.csv | Unseen test dataset for fraud prediction |

---

# Project Structure

```bash
MEDICARE_FRAUD_DETECTION/
│
├── data/
│   ├── raw/
│   │   ├── TRAIN1.csv
│   │   ├── TRAIN2.csv
│   │   └── TEST.csv
│   │
│   └── processed/
│
├── models/
│   ├── scaler.pkl
│   └── svm_fraud_model.pkl
│
├── notebooks/
│   ├── fraud_analysis_eda.ipynb
│   └── fraud_detection_model.ipynb
│
├── outputs/
│   ├── plots/
│   ├── feature_importance.csv
│   ├── predictions.csv
│   └── final_submission.csv
│
├── requirements.txt
└── README.md