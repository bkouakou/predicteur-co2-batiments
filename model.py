import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Charger les données (adapter le chemin)
data = pd.read_csv("/home/veone/Documents/OC/Consommateur_Batiement/df_resultat_analyse_batiments.csv")

# Sélection des variables explicatives et cible
features = ['Electricity(kBtu)', 'NaturalGas(kBtu)', 'BuildingAge',
            'Prop_LargestPropertyUseTypeGFA']
target = 'TotalGHGEmissions'

X = data[features]
y = data[target]

# Prétraitement
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entraînement
model = RandomForestRegressor()
model.fit(X_scaled, y)

# Sauvegarde
joblib.dump(model, 'model_co2.pkl')
joblib.dump(scaler, 'scaler_co2.pkl')