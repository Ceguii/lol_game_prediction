import time

from config import API_KEY, REGION, TAGLINE

from api_fetcher.enum_rank import High_Rank, Queue_games, Rank
from api_fetcher.api_data_fetcher import get_summoner_ID, get_puuid_from_summoner_ID, create_and_add_json_element, get_list_match_of_user, get_summoner_ID_low_elo, get_puuid_from_summoner_ID
from api_fetcher.parse_json import parse_json_summoner_ID, parse_json_summoner_ID_low_elo

def pipeline() -> None:
    
    
    # PIPELINE TESTE : VALIDÉ
    # À METTRE LE CODE PLUS TARD DANS LE FICHIER PIPELINE.PY
    
    try:
        """ print("\n/============================/")
        print("/=== PIPELINE CHALLENGER DATA ===/")
        print("/============================/\n")
        
        print("/============================/")
        print("/=== Obtenir les summonerIDs de toute les challengers ===/")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        ## AJOUTER LES ARGS
        json_format_player = get_summoner_ID(TAGLINE, API_KEY, High_Rank.CHALLENGER.value, Queue_games.RANKED_SOLO.value)
        time.sleep(2)
        
        # Parser this json to a list of summonerIDs
        summonerIDs = parse_json_summoner_ID(json_format_player)
        #print("La taille de la liste summonerIDs : ", len(summonerIDs))
        
        # List of puuid of each summonerIDs
        # On sélectionne 8 joueurs au hasard
        puuids = [get_puuid_from_summoner_ID(TAGLINE, API_KEY, summonerID) for summonerID in summonerIDs]
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
        print(f"Le temps d'exécution {High_Rank.CHALLENGER.name} a prit : {end_time - start_time}")
        #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
        print("/=== PIPELINE CHALLENGER TERMINER ===/")
        print("/=== FICHIER challenger_games.json ENREGISTRÉ\n")
        
        """ 
        #========================================================================================
        #========================================================================================
        """
        
        print("\n/============================/")
        print("/=== PIPELINE GRANDMASTER DATA ===/")
        print("/============================/\n")
        
        print("/============================/")
        print("/=== Obtenir les summonerIDs de toute les grandmaster ===/")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        ## AJOUTER LES ARGS
        json_format_player = get_summoner_ID(TAGLINE, API_KEY, High_Rank.GRAND_MASTER.value, Queue_games.RANKED_SOLO.value)
        time.sleep(2)
        
        # Parser this json to a list of summonerIDs
        summonerIDs = parse_json_summoner_ID(json_format_player)
        
        # List of puuid of each summonerIDs
        # On sélectionne 8 joueurs au hasard
        puuids = [get_puuid_from_summoner_ID(TAGLINE, API_KEY, summonerID) for summonerID in summonerIDs]
        time.sleep(2)
        #print(puuids)
            
        print("/============================/")
        print("/=== Création du fichier JSON stockant toutes les parties grandmaster ===/")
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
        
        start_time1 = time.time()
        
        for i in range(len(list_of_matchIDs)):
            print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
            for matchID in list_of_matchIDs[i]:
                create_and_add_json_element("grand_master.json", matchID, REGION, API_KEY)
            
            print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
            
        end_time1 = time.time()
        
        # Je fais 160 requetes pour 181 secondes, soit 61 secondes car 2 rate limite (TRÈS CORRECTE)
        print(f"Le temps d'exécution {High_Rank.GRAND_MASTER.name} a prit : {end_time1 - start_time1}")
        #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
        print("/=== PIPELINE GRANDMASTER TERMINER ===/")
        print("/=== FICHIER grand_master.json ENREGISTRÉ\n") """
        
        """ 
        ========================================================================================
        ========================================================================================
        """
        
        print("\n/============================/")
        print("/=== PIPELINE MASTER DATA ===/")
        print("/============================/\n")
        
        """ 
        ========================================================================================
        ========================================================================================
        """
        
        print("\n/============================/")
        print("/=== PIPELINE DIAMAND DATA ===/")
        print("/============================/\n")
        
        print("/============================/")
        print("/=== Obtenir les summonerIDs de toute les diamand ===/")
        print("/============================/\n")
        # Get all challenger summonerID in json format
        ## AJOUTER LES ARGS
        json_format_player = get_summoner_ID_low_elo(TAGLINE, API_KEY, Rank.DIAMOND.value, Queue_games.RANKED_SOLO.value)
        time.sleep(2)
        
        # Parser this json to a list of summonerIDs
        summonerIDs = parse_json_summoner_ID_low_elo(json_format_player)
        
        # List of puuid of each summonerIDs
        # On sélectionne 8 joueurs au hasard
        puuids = [get_puuid_from_summoner_ID(TAGLINE, API_KEY, summonerID) for summonerID in summonerIDs]
        time.sleep(2)
        #print(puuids)
            
        print("/============================/")
        print("/=== Création du fichier JSON stockant toutes les parties diamand ===/")
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
        
        start_time1 = time.time()
        
        for i in range(len(list_of_matchIDs)):
            print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
            for matchID in list_of_matchIDs[i]:
                create_and_add_json_element("diamand.json", matchID, REGION, API_KEY)
            
            print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
            
        end_time1 = time.time()
        
        # Je fais 160 requetes pour 181 secondes, soit 61 secondes car 2 rate limite (TRÈS CORRECTE)
        print(f"Le temps d'exécution {Rank.DIAMOND.name} a prit : {end_time1 - start_time1}")
        #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
        print("/=== PIPELINE DIAMAND TERMINER ===/")
        print("/=== FICHIER diamand.json ENREGISTRÉ\n")
        
    except Exception as e:
        print(f"Erreur dans la pipeline: {e}")

if __name__ == "__main__":
    
    pipeline()