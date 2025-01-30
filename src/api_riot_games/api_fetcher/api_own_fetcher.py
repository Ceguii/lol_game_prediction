import requests

from .handle_api_error import handle_api_error

def get_puuid(region: str, api: str, riot_id: str, tagline: str) -> str:
    """Obtenir le PUUID à partir du Riot ID (Nom d'invocateur + Tag) """
    
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tagline}"
    headers = {"X-Riot-Token": api}
    
    try:
        # Effectuer la requête HTTP
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        print(response.json())
        return response.json()["puuid"]
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")