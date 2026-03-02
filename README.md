# 🏦 Customer Churn Prediction System

An end-to-end Machine Learning system for predicting customer churn risk using XGBoost, FastAPI, and Streamlit.

---

## 🔗 Live Demo

👉 **Try the Streamlit App:**  


---

## 🚀 Project Overview

This project builds a complete ML pipeline to:

- Predict customer churn probability
- Categorize customers into Low / Medium / High risk
- Serve predictions via FastAPI
- Provide an interactive Streamlit web interface

The system is designed to simulate real-world ML deployment in an insurance/business setting.

---

## 🏗 Architecture

### Cloud Version
User → Streamlit → ML Pipeline (.pkl) → Prediction

### Local API Version
User → Streamlit → FastAPI → ML Pipeline → Prediction

---

## 📊 Model Development

- Data preprocessing using:
  - StandardScaler
  - OneHotEncoder
  - ColumnTransformer
- Compared models:
  - Logistic Regression
  - Random Forest
  - XGBoost
- Model selection via 5-fold Cross Validation (ROC-AUC)
- Final Model: **XGBoost**
- Test ROC-AUC: ~0.86

---

## 📁 Project Structure
churn-ml-system/
│
├── README.md
├── .gitignore
│── churn_pipeline.pkl
│── main.py
│── requirements.txt
│── streamlit_app.py
│
├───fastAPI
│       streamlit_fastapi.py
│
└───notebook
        Churn_Modelling_notebook.ipynb
