# 1. Utiliser une image de base Python officielle et légère
FROM python:3.10-slim

# 2. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3. Copier le fichier des dépendances
COPY requirements.txt .

# 4. Installer les dépendances
# --no-cache-dir réduit la taille de l'image
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le code de l'application
COPY app.py .

# 6. Commande à exécuter lorsque le conteneur démarre
CMD ["python", "app.py"]
