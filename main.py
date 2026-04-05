from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model and columns
model = joblib.load("models/pricing_model.pkl")
columns = joblib.load("models/columns.pkl")

# Input schema
class InputData(BaseModel):
    rating: float
    demand: float
    category: str

@app.get("/")
def home():
    return {"message": "Smart Pricing API Running 🚀"}

@app.post("/predict-price")
def predict(data: InputData):

    # Convert input to dataframe
    df = pd.DataFrame([{
        "rating": data.rating,
        "demand": data.demand,
        "category": data.category
    }])

    # One-hot encoding
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=columns, fill_value=0)

    # Prediction
    prediction = model.predict(df)

    return {"predicted_price": float(prediction[0])}