""" 

    FICHIER MAIN POUR TESTER ET PRENDRE CONNAISSANCE DE L'API RIOT GAMES

"""

import requests
import os
import time
from dotenv import load_dotenv
from typing import List

load_dotenv()
    
API_KEY = os.getenv("API_KEY")
REGION = os.getenv("REGION")
RIOT_ID = os.getenv("RIOT_ID")
TAGLINE = os.getenv("TAGLINE")

def handle_api_error(response: requests.Response) -> None:
    """ 
        Gère les erreurs de l'API en fonction du code de statut de la réponse.
        À voir sur le site developer.riotgames
    """
    
    if response.status_code == 200:
        return  # Pas d'erreur, succès.
    elif response.status_code == 400:
        raise Exception("Bad Request - Requête mal formée.")
    elif response.status_code == 401:
        raise Exception("Unauthorized - Clé API invalide ou manquante.")
    elif response.status_code == 403:
        raise Exception("Forbidden - Accès interdit, vérifiez vos autorisations.")
    elif response.status_code == 404:
        raise Exception("Not Found - Données introuvables.")
    elif response.status_code == 405:
        raise Exception("Method Not Allowed - La méthode HTTP utilisée est interdite.")
    elif response.status_code == 415:
        raise Exception("Unsupported Media Type - Le type de média n'est pas pris en charge.")
    elif response.status_code == 429:
        print("Rate Limit Exceeded - Limite de requêtes atteinte. Attente de 60 secondes...")
        time.sleep(60)  # Attente de 60 secondes avant de réessayer
    elif response.status_code == 500:
        raise Exception("Internal Server Error - Erreur interne du serveur Riot.")
    elif response.status_code == 502:
        raise Exception("Bad Gateway - Problème avec la passerelle.")
    elif response.status_code == 503:
        raise Exception("Service Unavailable - Le service est temporairement indisponible.")
    elif response.status_code == 504:
        raise Exception("Gateway Timeout - Délai d'attente de la passerelle expiré.")
    else:
        raise Exception(f"Erreur {response.status_code} - Erreur inconnue.")

import requests

def get_puuid(riot_id: str, tagline: str) -> str:
    """Obtenir le PUUID à partir du Riot ID (Nom d'invocateur + Tag)."""
    
    url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{riot_id}/{tagline}"
    headers = {"X-Riot-Token": API_KEY}
    
    try:
        # Effectuer la requête HTTP
        response = requests.get(url, headers=headers)
        
        handle_api_error(response)
        
        print(response.json())

        return response.json()["puuid"]
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")


def get_list_match_of_user(puuid: str) -> List[str]:
    """ Récupérer les IDs des matchs d'un joueur """
    
    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}"
    headers = {"X-Riot-Token": API_KEY}
    
    try:
        # Effectuer la requête
        response = requests.get(url, headers=headers)
        
        handle_api_error(response)
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête : {str(e)}")
    
    # Retourner une liste vide en cas d'erreur
    return []

def main() -> None:
    
    # Obtenir le PUUID à partir du Riot ID et du Tagline
    """ puuid = get_puuid(RIOT_ID, TAGLINE)
    print("/=====================/")
    print(f"PUUID : {puuid}")
    print("/=====================/")
    list_match_ids = get_list_match_of_user(puuid)
    print(list_match_ids) """
    
    student = {
        "no": 1020,
        "name": "Mike Taylor",
        "age": [
            {
                "caca": "crotte",
                "pipi": "liquide"
            },
            {
                "caca": "cailloux",
                "pipi": "eau"
            },
            {
                "caca": "cailloux",
                "pipi": "eau"
            }
        ]
    }
    
    #print(student['age'][0]['caca'])
    
    print(len(student.get("age")))
    
if __name__ == "__main__":
    
    main()
