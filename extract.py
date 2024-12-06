import requests

def extract_data(url, params):
    """Fonction d'extraction de données depuis l'API."""
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur dans la requête API : {response.status_code}")
        return None
