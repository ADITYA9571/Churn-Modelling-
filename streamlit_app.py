import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load("churn_pipeline.pkl")

model = load_model()

st.title("Customer Churn Prediction System")
st.write("Enter customer details below to estimate churn probability.")

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
num_products = st.number_input("Number of Products", min_value=1, max_value=4, value=1)
has_card = st.selectbox("Has Credit Card", [0, 1])
active_member = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

if st.button("Predict Churn"):

    input_data = {
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_card,
        "IsActiveMember": active_member,
        "EstimatedSalary": salary
    }

    input_df = pd.DataFrame([input_data])

    prob = model.predict_proba(input_df)[0][1]

    # Risk categorization
    if prob > 0.7:
        prediction = "High Risk"
    elif prob > 0.4:
        prediction = "Medium Risk"
    else:
        prediction = "Low Risk"

    st.subheader("Prediction Result")
    st.write(f"Churn Probability: **{round(float(prob), 4)}**")

    st.progress(float(prob))

    if prediction == "High Risk":
        st.error(f"Risk Level: {prediction}")
    elif prediction == "Medium Risk":
        st.warning(f"Risk Level: {prediction}")
    else:
        st.success(f"Risk Level: {prediction}")