from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(
    title="House Price Prediction API",
    description="ML-powered API for predicting house prices",
    version="1.0.0"
)

# Load the trained model
model = joblib.load("model/house_price_model.pkl")


class HouseInput(BaseModel):
    area_sqft: float
    bedrooms: int
    bathrooms: int
    parking: int


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict_price(house: HouseInput):
    features = np.array([[
        house.area_sqft,
        house.bedrooms,
        house.bathrooms,
        house.parking
    ]])

    prediction = model.predict(features)[0]

    return {
        "predicted_price_lakh": round(float(prediction), 2)
    }
