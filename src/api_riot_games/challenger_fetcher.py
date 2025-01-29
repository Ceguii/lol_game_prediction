import os
import sys
import time
import random
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from typing import List
from api_data_fetcher import get_list_match_of_user, get_matchs_details_from_matchID, create_and_add_json_element
from handle_api_error import handle_api_error
from config import API_KEY, TAGLINE, REGION

def parse_json_challenger(json_str: dict) -> List[str]:
    
    if len(json_str) == 0:
        return []
    
    result_list = []
    entries_size = len(json_str.get("entries"))
    
    for i in range(entries_size - 1):
        result_list.append(json_str['entries'][i]['summonerId'])
        
    return random.sample(result_list, 8)

def get_challenger_summonID(tagline: str, api: str) -> dict:
    
    """ Obtenir la liste des joueurs de rang Challenger dans la catégories LEAGUE-V4 """
    
    url = f"https://{tagline}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        handle_api_error(response)
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")
    
def get_puuid_from_summonerID(tagline: str, api: str, summonerID: str):
    """ Obtenir le puuid à partir du summonerID (Dans le cas Challenger)"""
    
    url = f"https://{tagline}.api.riotgames.com/lol/summoner/v4/summoners/{summonerID}?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        #handle_api_error(response)
        return response.json()['puuid']
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")
    
def main() -> None:
    
    try:
        print("\n/============================/")
        print("=== PIPELINE CHALLENGER DATA ===")
        print("/============================/\n")
        time.sleep(1)
        
        print("/============================/")
        print("=== Obtenir les summonerIDs de toute les challengers ===")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        json_str = get_challenger_summonID(TAGLINE, API_KEY)
        time.sleep(1)
        
        # Parser this json to a list of summonerIDs
        summonerIDs = parse_json_challenger(json_str)
        #print("La taille de la liste summonerIDs : ", len(summonerIDs))
        
        print("/============================/")
        print("/=== Affichage des puuids ===/")
        print("/============================/\n")
        
        # List of puuid of each summonerIDs
        # On sélectionne 8 joueurs au hasard
        puuids = [get_puuid_from_summonerID(TAGLINE, API_KEY, summonerID) for summonerID in summonerIDs]
        #print(puuids)
            
        print("/============================/")
        print("/=== Création du fichier JSON stockant toutes les parties challenger ===")
        print("/============================/\n")
        
        # Modifier l'url sur le COUNT, pour l'instant COUNT=20
        # /!\ Vu qu'on a selectionné 8 joueurs, chaque joueur aura 100 parties.
        # soit un total de 800 parties
        # Liste de liste : [[matchIDs], [""]]
        list_of_matchIDs = [get_list_match_of_user(REGION, API_KEY, puuid) for puuid in puuids]
        #print(matchIDs)
        
        print("/============================/")
        print("=== Récupération des matches sous format JSON ===")
        print("/============================/\n")
        
        # Test avec un matchID et on recuperer le match details avec la fonction
        # get_matchs_details_from_matchID
        
        for matchIDs in list_of_matchIDs:
            for matchID in matchIDs:
                create_and_add_json_element("challenger_games.json", matchID)
            
        print("/=== PIPELINE CHALLENGER TERMINER ===/")
        print("/=== FICHIER challenger_games.json ENREGISTRÉ\n")
        
    except Exception as e:
        print(f"Erreur dans la pipeline: {e}")

if __name__ == "__main__":
    
    main()