import streamlit as st
import requests

st.title("Prédiction des émissions de CO₂ d'un bâtiment")

# Saisie utilisateur
electricity = st.number_input("Consommation électrique (kBtu)", min_value=0.0)
gas = st.number_input("Consommation gaz (kBtu)", min_value=0.0)
age = st.number_input("Âge du bâtiment (années)", min_value=0.0)
prop_gfa = st.number_input("Proportion de la surface principale (0-1)", min_value=0.0, max_value=1.0)

if st.button("Prédire"):
    payload = {
        "electricity": electricity,
        "gas": gas,
        "age": age,
        "prop_gfa": prop_gfa
    }
    response = requests.post("http://localhost:8000/predict", json=payload)
    if response.status_code == 200:
        st.success(f"Estimation des émissions de CO₂ : {response.json()['prediction_CO2']:.2f} tonnes")
    else:
        st.error("Erreur lors de la prédiction")