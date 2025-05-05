# Utilise une image officielle légère avec Python
FROM python:3.10-slim

# Crée un répertoire de travail
WORKDIR /app

# Copie les fichiers du projet dans le conteneur
COPY . /app

# Installe les dépendances
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose le port utilisé par Streamlit
EXPOSE 8501

# Commande de lancement de Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
