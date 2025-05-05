# 2. --- main.py ---
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model_co2.pkl")
scaler = joblib.load("scaler_co2.pkl")

class BuildingFeatures(BaseModel):
    electricity: float
    gas: float
    age: float
    prop_gfa: float

@app.post("/predict")
def predict_co2(features: BuildingFeatures):
    input_data = np.array([[features.electricity, features.gas, features.age, features.prop_gfa]])
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)
    return {"prediction_CO2": float(prediction[0])}