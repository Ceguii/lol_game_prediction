import os
import sys
import time
import random
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from typing import List
from api_data_fetcher import get_list_match_of_user, create_and_add_json_element
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
    
    # PIPELINE TESTE : VALIDÉ
    # À METTRE LE CODE PLUS TARD DANS LE FICHIER PIPELINE.PY
    
    try:
        print("\n/============================/")
        print("=== PIPELINE CHALLENGER DATA ===")
        print("/============================/\n")
        
        print("/============================/")
        print("=== Obtenir les summonerIDs de toute les challengers ===")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        json_str = get_challenger_summonID(TAGLINE, API_KEY)
        time.sleep(2)
        
        # Parser this json to a list of summonerIDs
        summonerIDs = parse_json_challenger(json_str)
        #print("La taille de la liste summonerIDs : ", len(summonerIDs))
        
        print("/============================/")
        print("/=== Affichage des puuids ===/")
        print("/============================/\n")
        
        # List of puuid of each summonerIDs
        # On sélectionne 8 joueurs au hasard
        puuids = [get_puuid_from_summonerID(TAGLINE, API_KEY, summonerID) for summonerID in summonerIDs]
        time.sleep(2)
        #print(puuids)
            
        print("/============================/")
        print("/=== Création du fichier JSON stockant toutes les parties challenger ===")
        print("/============================/\n")
        
        # Modifier l'url sur le COUNT, pour l'instant COUNT=20
        # /!\ Vu qu'on a selectionné 8 joueurs, chaque joueur aura 100 parties.
        # soit un total de 800 parties
        # Liste de liste : [[matchIDs], [""]]
        list_of_matchIDs = [get_list_match_of_user(REGION, API_KEY, puuid) for puuid in puuids]
        time.sleep(2)
        #print(matchIDs)
        
        print("/============================/")
        print("=== Récupération des matches sous format JSON ===")
        print("/============================/\n")
        
        start_time = time.time()
        count_secondes = 0
        
        # Test avec un matchID et on recuperer le match details avec la fonction
        # get_matchs_details_from_matchID
        
        # Ce code fonctionne...
        """ for matchIDs in list_of_matchIDs:
            for i in range(len(matchIDs)):
                print(f"-- Obtention des parties du joueur {i} en cours... --")
                create_and_add_json_element("challenger_games.json", matchIDs[i])
                print(f"-- Obtention des parties du joueur {i} terminé --\n")
                time.sleep(1) """
        
        # Code bon
        for i in range(len(list_of_matchIDs)):
            print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
            for matchID in list_of_matchIDs[i]:
                create_and_add_json_element("challenger_games.json", matchID)
                #count_secondes += 0.5
                #time.sleep(0.5)
            
            print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
            
        end_time = time.time()
        
        # Je fais 160 requetes pour 181 secondes, soit 61 secondes car 2 rate limite (TRÈS CORRECTE)
        print(f"Le temps d'exécution a prit : {end_time - start_time}")
        #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
        print("/=== PIPELINE CHALLENGER TERMINER ===/")
        print("/=== FICHIER challenger_games.json ENREGISTRÉ\n")
        
        # Fichier challenger_games.json fait 25Mo, ce qui n'est pas trop énorme...
        
    except Exception as e:
        print(f"Erreur dans la pipeline: {e}")

if __name__ == "__main__":
    
    main()