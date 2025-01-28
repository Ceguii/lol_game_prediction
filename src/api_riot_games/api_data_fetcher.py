import os
import sys
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from typing import List
from handle_api_error import handle_api_error
from config import API_KEY, REGION, RIOT_ID, TAGLINE

# Rank inférieur à Master

def get_puuid(region: str, api: str, riot_id: str, tagline: str) -> str:
    """Obtenir le PUUID à partir du Riot ID (Nom d'invocateur + Tag) RANK INFÉRIEUR À DIAMAND"""
    
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


def get_list_match_of_user(region: str, api: str, puuid: str) -> List[str]:
    """ Récupérer les IDs des matchs d'un joueur à partir d'un PUUID """
    
    # /!\ Changer le nombre de count à 100
    # Pour l'instant count est à 20 pour le teste
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        # Effectuer la requête
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête : {str(e)}")
    
    # Retourner une liste vide en cas d'erreur
    return []

def get_matchs_details_from_matchID(region: str, matchID: str, api: str):
    """  """
    
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        # Effectuer la requête
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête : {str(e)}")