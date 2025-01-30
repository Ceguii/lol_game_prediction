import time

from config import API_KEY, REGION, TAGLINE

from api_fetcher.enum_rank import High_Rank, Queue_games
from api_fetcher.api_data_fetcher import get_summonID, parse_json_challenger, get_puuid_from_summonerID, create_and_add_json_element, get_list_match_of_user

def pipeline() -> None:
    
    
    # PIPELINE TESTE : VALIDÉ
    # À METTRE LE CODE PLUS TARD DANS LE FICHIER PIPELINE.PY
    
    try:
        print("\n/============================/")
        print("/=== PIPELINE CHALLENGER DATA ===/")
        print("/============================/\n")
        
        print("/============================/")
        print("/=== Obtenir les summonerIDs de toute les challengers ===/")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        ## AJOUTER LES ARGS
        json_str = get_summonID(TAGLINE, API_KEY, High_Rank.CHALLENGER.value, Queue_games.RANKED_SOLO.value)
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
        print("/=== Création du fichier JSON stockant toutes les parties challenger ===/")
        print("/============================/\n")
        
        # Modifier l'url sur le COUNT, pour l'instant COUNT=20
        # /!\ Vu qu'on a selectionné 8 joueurs, chaque joueur aura 100 parties.
        # soit un total de 800 parties
        # Liste de liste : [[matchIDs], [""]]
        list_of_matchIDs = [get_list_match_of_user(REGION, API_KEY, puuid) for puuid in puuids]
        time.sleep(2)
        #print(matchIDs)
        
        print("/============================/")
        print("/=== Récupération des matches sous format JSON ===/")
        print("/============================/\n")
        
        start_time = time.time()
        
        for i in range(len(list_of_matchIDs)):
            print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
            for matchID in list_of_matchIDs[i]:
                create_and_add_json_element("challenger_games.json", matchID, REGION, API_KEY)
            
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
    
    pipeline()