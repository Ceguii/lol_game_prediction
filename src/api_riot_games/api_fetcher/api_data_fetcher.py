import json
import time
import random
import requests

from typing import Any, Dict, List
from .handle_api_error import handle_api_error

# Pour high elo
def get_summoner_ID(tagline: str, api: str, league: str, queue: str) -> List[Dict[str, Any]]:
    
    """ Obtenir la liste des joueurs dans la catégories LEAGUE-V4 """
    
    url = f"https://{tagline}.api.riotgames.com/lol/league/v4/{league}/by-queue/{queue}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")
    

def get_summoner_ID_low_elo(tagline: str, api: str, league: str, queue: str) -> List[Dict[str, Any]]:

    division = random.choice(["I", "II", "III", "IV"])

    url = f"https://{tagline}.api.riotgames.com/lol/league/v4/entries/{queue}/{league}/{division}?page={1}&api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")
    

# Dans le cas ou c'est low_elo, il faudra faire attention et donner plus de temps pour eviter
# de rate limite exceed
def get_puuid_from_summoner_ID(tagline: str, api: str, summonerID: str) -> str:
    
    """ Obtenir le puuid à partir du summonerID """
    
    url = f"https://{tagline}.api.riotgames.com/lol/summoner/v4/summoners/{summonerID}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        print(response.json())
        ## Trouver une solution pour ne pas rate limit
        # À voir...
        time.sleep(0.2)
        return response.json()['puuid']
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")

## Fonctions générales pour les API Riot Games

def create_and_add_json_element(file_name: str, elt: dict, region: str, api: str) -> None:
    # Charger les données existantes
    try:
        with open("../../data/raw/" + file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []  # Si le fichier n'existe pas, on crée une nouvelle liste vide

    # Ajouter le nouvel élément (match details à partir du matchID)
    data.append(get_matchs_details_from_match_ID(region, elt, api))

    # Sauvegarder les données dans le fichier JSON
    with open("../../data/raw/" + file_name, 'w') as f:
        json.dump(data, f, indent=4)
        

def get_list_match_of_user(region: str, api: str, puuid: str) -> List[str]:
    """ Récupérer les IDs des matchs d'un joueur à partir d'un PUUID """
    
    # /!\ Changer le nombre de count à 100
    # Pour l'instant count est à 20 pour le teste
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={20}&api_key={api}"
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


def get_matchs_details_from_match_ID(region: str, matchID: str, api: str) -> List[Dict[str, Any]]:
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