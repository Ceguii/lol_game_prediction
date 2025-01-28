import os
import requests
from typing import List
from config import API_KEY, TAGLINE  # Assure-toi que ces variables sont bien dans config.py
from api_riot_games.handle_api_error import handle_api_error  # Assure-toi que le chemin est correct

# Fonction pour parser le JSON de challenger et récupérer les summoner IDs
def parse_json_challenger(json_str: dict) -> List[str]:
    if len(json_str) == 0:
        return []
    
    result_list = []
    entries_size = len(json_str.get("entries"))
    
    # Note: Les indices commencent à 0, donc il faut bien boucler jusqu'à `entries_size` et pas `entries_size - 1`
    for i in range(entries_size):
        result_list.append(json_str['entries'][i]['summonerId'])
        
    return result_list

# Fonction pour récupérer les données de l'API Riot Games
def get_challenger_summonID(tagline: str, api: str) -> dict:
    """Obtenir la liste des joueurs de rang Challenger dans la catégorie LEAGUE-V4"""
    
    url = f"https://{tagline}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={api}"
    headers = {"X-Riot-Token": api}
    
    try:
        response = requests.get(url, headers=headers)
        handle_api_error(response)  # Vérifie si la réponse contient une erreur
        print(type(response.json()))
        return response.json()
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Une erreur est survenue lors de la requête HTTP : {str(e)}")

# Fonction principale
def main() -> None:
    try:
        # Récupérer tous les Challenger SummonerID au format JSON
        json_str = get_challenger_summonID(TAGLINE, API_KEY)
        
        # Parser ce JSON pour obtenir une liste de SummonerID
        summonerID_list = parse_json_challenger(json_str)
        print(f"Nombre de SummonerIDs : {len(summonerID_list)}")
        
    except Exception as e:
        print(f"Erreur dans la pipeline: {e}")

# Exécution du script principal
if __name__ == "__main__":
    main()
