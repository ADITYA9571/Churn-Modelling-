import streamlit as st
import requests

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")

st.title("Customer Churn Prediction")
st.write("Enter customer details below to predict churn risk.")

# Input fields
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

    response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        prob = result["churn_probability"]
        prediction = result["prediction"]

        st.subheader("Prediction Result")
        st.write(f"Churn Probability: **{prob}**")

        if prediction == "High Risk":
            st.error(f"Risk Level: {prediction}")
        elif prediction == "Medium Risk":
            st.warning(f"Risk Level: {prediction}")
        else:
            st.success(f"Risk Level: {prediction}")
    else:
        st.error("API connection failed. Make sure FastAPI is running.")