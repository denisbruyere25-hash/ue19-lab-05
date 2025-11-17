# ue19-lab-05

Ceci est une simple application Python 3 qui interroge [JokeAPI](https://v2.jokeapi.dev/) pour afficher une blague aléatoire. Le projet est conteneurisé à l'aide de Docker.

## Fonctionnalités

* Interroge une API publique de blagues.
* Affiche la blague dans le terminal.
* Peut être exécuté localement avec Python ou via un conteneur Docker.

## Prérequis

* [Python 3.7+](https://www.python.org/)
* [Docker](https://www.docker.com/) (pour l'exécution via Docker)

---

## Installation (Locale)

1.  Clonez ce repository :
    ```bash
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/ue19-lab-05.git](https://github.com/VOTRE_NOM_UTILISATEUR/ue19-lab-05.git)
    cd ue19-lab-05
    ```

2.  (Optionnel) Créez et activez un environnement virtuel :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3.  Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

---

## Comment lancer l'application (How-To)

Vous avez deux façons de lancer le programme :

### Option 1 : Directement avec Python

Après avoir suivi les étapes d'installation locale, exécutez simplement :

```bash
python app.py
```

### Option 2 : Avec Docker

Si Docker est installé, vous pouvez construire l'image et l'exécuter.

1.  **Construire l'image Docker** (Assurez-vous d'être à la racine du projet) :
    ```bash
    docker build -t blague-app .
    ```

2.  **Exécuter le conteneur** :
    ```bash
    docker run --rm blague-app
    ```
