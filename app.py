import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Charger le modèle et le scaler
model = joblib.load("model_co2.pkl")
scaler = joblib.load("scaler_co2.pkl")

st.title("Prédiction des émissions de CO₂")

electricity = st.number_input("Consommation électrique (kBtu)", min_value=0.0)
gas = st.number_input("Consommation gaz (kBtu)", min_value=0.0)
age = st.number_input("Âge du bâtiment", min_value=0.0)
prop_gfa = st.number_input("Prop. surface principale (0-1)", min_value=0.0, max_value=1.0)
# Prédiction
if st.button("Prédire"):
    data = np.array([[electricity, gas, age, prop_gfa]])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    st.success(f"Émissions de CO₂ estimées : {prediction[0]:.2f} tonnes")
