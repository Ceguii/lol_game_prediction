import os
import json
import random
import requests

from typing import List

from .handle_api_error import handle_api_error
from config import API_KEY, REGION

def parse_json_challenger(json_str: dict) -> List[str]:
    
    if len(json_str) == 0:
        return []
    
    result_list = []
    entries_size = len(json_str.get("entries"))
    
    for i in range(entries_size - 1):
        result_list.append(json_str['entries'][i]['summonerId'])
        
    return random.sample(result_list, 8)


def get_summonID(tagline: str, api: str, league: str, queue: str) -> dict:
    
    """ Obtenir la liste des joueurs dans la catégories LEAGUE-V4 """
    
    url = f"https://{tagline}.api.riotgames.com/lol/league/v4/{league}/by-queue/{queue}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")
    
    
def get_puuid_from_summonerID(tagline: str, api: str, summonerID: str):
    """ Obtenir le puuid à partir du summonerID """
    
    url = f"https://{tagline}.api.riotgames.com/lol/summoner/v4/summoners/{summonerID}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        #handle_api_error(response)
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
    data.append(get_matchs_details_from_matchID(region, elt, api))

    # Sauvegarder les données dans le fichier JSON
    with open("../../data/raw/" + file_name, 'w') as f:
        json.dump(data, f, indent=4)
        
        

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