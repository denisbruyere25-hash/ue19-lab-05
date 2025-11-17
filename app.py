import requests
import sys


def get_joke():
    """
    Interroge JokeAPI pour une blague en une seule partie (type=single)
    et l'affiche sur la console.
    """
    # URL de l'API pour une blague "single" (en une partie)
    url = "https://v2.jokeapi.dev/joke/Any?type=single"

    try:
        # Exécute la requête GET
        response = requests.get(url, timeout=10)

        # Lève une exception si la requête a échoué (code 4xx ou 5xx)
        response.raise_for_status()

        # Convertit la réponse JSON en dictionnaire Python
        data = response.json()

        if data["error"]:
            print(f"Erreur de l'API : {data.get('message', 'Erreur inconnue')}")
        else:
            print("----- Blague du jour -----")
            print(data["joke"])
            print("--------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API : {e}")
        sys.exit(1)  # Sortir avec un code d'erreur


if __name__ == "__main__":
    get_joke()