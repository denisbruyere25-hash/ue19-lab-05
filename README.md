# ue19-lab-05 : Application de Blagues

Application Python 3 qui interroge JokeAPI et est conteneurisée avec Docker.

## Installation Locale

1. Clonez le projet.
2. Installez les dépendances : `pip install -r requirements.txt`

## Lancer (How-to)

### Avec Python localement
```bash
python app.py
```

### Avec Docker
1. Construire l'image :
   ```bash
   docker build -t blague-app .
   ```
2. Exécuter le conteneur :
   ```bash
   docker run --rm blague-app
   ```
