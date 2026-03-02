from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Customer Churn Prediction API")

model = joblib.load("churn_pipeline.pkl")

class CustomerData(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


@app.post("/predict")
def predict(data: CustomerData):

    input_df = pd.DataFrame([data.dict()])

    prob = model.predict_proba(input_df)[0][1]
    if prob > 0.7:
        risk = "High Risk"
    elif prob > 0.4:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    return {
        "churn_probability": round(float(prob), 4),
        "prediction": risk
    }