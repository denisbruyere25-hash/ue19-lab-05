import requests
import sys

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data["error"]:
            print(f"Erreur de l'API : {data.get('message', 'Erreur inconnue')}")
        else:
            print("----- Blague du jour -----")
            print(data["joke"])
            print("--------------------------")
            
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la connexion à l'API : {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_joke()
