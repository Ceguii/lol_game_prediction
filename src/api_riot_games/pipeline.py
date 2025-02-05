import time

from config import API_KEY, REGION, TAGLINE

from api_fetcher.enum_rank import High_Rank, Queue_games, Rank
from api_fetcher.api_data_fetcher import get_summoner_ID, get_puuid_from_summoner_ID, create_and_add_json_element, get_list_match_of_user, get_summoner_ID_low_elo, get_puuid_from_summoner_ID, get_matchs_details_from_match_ID_timeline
from api_fetcher.parse_json import parse_json_summoner_ID, parse_json_summoner_ID_low_elo
from api_fetcher.rate_limiter import rate_limited_request
from database_utils import create_database, create_matches_table, insert_data_into_db


""" /=============================================================================/ """
""" /=============================================================================/ """
""" /=============================================================================/ """

def challenger() -> None:
    
    print("\n/============================/")
    print("/=== PIPELINE CHALLENGER DATA ===/")
    print("/============================/\n")
        
    print("/============================/")
    print("/=== Obtenir les summonerIDs de toute les challengers ===/")
    print("/============================/\n")
    
    json_format_player = rate_limited_request(
        get_summoner_ID, TAGLINE, API_KEY, High_Rank.CHALLENGER.value, Queue_games.RANKED_SOLO.value
    )        
    
    print("/============================/")
    print("/=== SummonerIDs des joueurs Challenger récupéré avec SUCCÈS ===/")
    print("/============================/\n")
    
    print("/============================/")
    print("/=== Obtiention d'une liste des summonerIDs (PARSER) ===/")
    print("/============================/\n")
        
    summonerIDs = parse_json_summoner_ID(json_format_player)
        
    print("/============================/")
    print("/=== Récupération de liste des PUUIDS de chaque joueur sélectionné ===/")
    print("/============================/\n")    
        
    # List of puuid of each summonerIDs
    # On sélectionne 8 joueurs au hasard
       
    puuids = [
        rate_limited_request(get_puuid_from_summoner_ID, TAGLINE, API_KEY, summonerID)
        for summonerID in summonerIDs
    ]
            
    print("/============================/")
    print("/=== Récupération des Match IDs pour chaque PUUID ===/")
    print("/============================/\n")
        
    # Modifier l'url sur le COUNT, pour l'instant COUNT=20
    # /!\ Vu qu'on a selectionné 8 joueurs, chaque joueur aura 100 parties.
    # soit un total de 800 parties
    # Liste de liste : [[matchIDs], [""]]
       
    list_of_matchIDs = [
        rate_limited_request(get_list_match_of_user, REGION, API_KEY, puuid)
        for puuid in puuids
    ]
        
    print(f"Total de joueurs : {len(list_of_matchIDs)}")
    print(f"Total de matche par joueur : {len(list_of_matchIDs[0])}\n")

    print("/============================/")
    print("/=== Création du fichier JSON stockant toutes les parties Diamond ===/")
    print("/============================/\n")
        
    start_time = time.time()
        
    for i in range(len(list_of_matchIDs)):
        print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
        for matchID in list_of_matchIDs[i]:
            rate_limited_request(create_and_add_json_element, "challenger_games.json", matchID, REGION, API_KEY)
            
        print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
            
    end_time = time.time()
        
    # Je fais 160 requetes pour 181 secondes, soit 61 secondes car 2 rate limite (TRÈS CORRECTE)
    print(f"Le temps d'exécution {High_Rank.CHALLENGER.name} a pris : {end_time - start_time:.2f} secondes")
    #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
    print("/=== PIPELINE CHALLENGER TERMINER ===/")
    print("/=== FICHIER challenger_games.json ENREGISTRÉ\n")
    
    
def grand_master() -> None:
    
    print("\n/============================/")
    print("/=== PIPELINE GRANDMASTER DATA ===/")
    print("/============================/\n")
        
    print("/============================/")
    print("/=== Obtenir les summonerIDs de toute les grandmaster ===/")
    print("/============================/\n")
    
    json_format_player = rate_limited_request(
        get_summoner_ID, TAGLINE, API_KEY, High_Rank.GRAND_MASTER.value, Queue_games.RANKED_SOLO.value
    )        
    
    print("/============================/")
    print("/=== SummonerIDs des joueurs GrandMaster récupéré avec SUCCÈS ===/")
    print("/============================/\n")
    
    print("/============================/")
    print("/=== Obtiention d'une liste des summonerIDs (PARSER) ===/")
    print("/============================/\n")
        
    summonerIDs = parse_json_summoner_ID(json_format_player)
        
    print("/============================/")
    print("/=== Récupération de liste des PUUIDS de chaque joueur sélectionné ===/")
    print("/============================/\n")    
        
    # List of puuid of each summonerIDs
    # On sélectionne 8 joueurs au hasard
       
    puuids = [
        rate_limited_request(get_puuid_from_summoner_ID, TAGLINE, API_KEY, summonerID)
        for summonerID in summonerIDs
    ]
            
    print("/============================/")
    print("/=== Récupération des Match IDs pour chaque PUUID ===/")
    print("/============================/\n")
        
    # Modifier l'url sur le COUNT, pour l'instant COUNT=20
    # /!\ Vu qu'on a selectionné 8 joueurs, chaque joueur aura 100 parties.
    # soit un total de 800 parties
    # Liste de liste : [[matchIDs], [""]]
       
    list_of_matchIDs = [
        rate_limited_request(get_list_match_of_user, REGION, API_KEY, puuid)
        for puuid in puuids
    ]
        
    print(f"Total de joueurs : {len(list_of_matchIDs)}")
    print(f"Total de matche par joueur : {len(list_of_matchIDs[0])}\n")

    print("/============================/")
    print("/=== Création du fichier JSON stockant toutes les parties GrandMaster ===/")
    print("/============================/\n")
        
    start_time = time.time()
        
    for i in range(len(list_of_matchIDs)):
        print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
            
        for matchID in list_of_matchIDs[i]:
            rate_limited_request(create_and_add_json_element, "grand_master.json", matchID, REGION, API_KEY)
            
        print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
            
    end_time = time.time()
        
    # Je fais 160 requetes pour 181 secondes, soit 61 secondes car 2 rate limite (TRÈS CORRECTE)
    print(f"Le temps d'exécution {High_Rank.GRAND_MASTER.name} a pris : {end_time - start_time:.2f} secondes")
    #print(f"Le temps d'exécution sans compter les 1 seconde à chaque itération de joueur : {end_time - start_time - count_secondes}")
            
    print("/=== PIPELINE GRANDMASTER TERMINER ===/")
    print("/=== FICHIER grand_master.json ENREGISTRÉ\n")


def diamond() -> None:
    
    print("\n/============================/")
    print("/=== PIPELINE DIAMOND DATA ===/")
    print("/============================/\n")

    print("/============================/")
    print("/=== Obtenir les dicts contenant les summonerIDs des joueurs Diamond ===/")
    print("/============================/\n")

    json_format_player = rate_limited_request(
        get_summoner_ID_low_elo, TAGLINE, API_KEY, Rank.DIAMOND.value, Queue_games.RANKED_SOLO.value
    )

    print("/============================/")
    print("/=== SummonerIDs des joueurs Diamond récupéré avec SUCCÈS ===/")
    print("/============================/\n")

    print("/============================/")
    print("/=== Obtiention d'une liste des summonerIDs (PARSER) ===/")
    print("/============================/\n")

    summonerIDs = parse_json_summoner_ID_low_elo(json_format_player)

    print("/============================/")
    print("/=== Récupération de liste des PUUIDS de chaque joueur sélectionné ===/")
    print("/============================/\n")

    puuids = [
        rate_limited_request(get_puuid_from_summoner_ID, TAGLINE, API_KEY, summonerID)
        for summonerID in summonerIDs
    ]
    
    print("/============================/")
    print("/=== Récupération des Match IDs pour chaque PUUID ===/")
    print("/============================/\n")

    list_of_matchIDs = [
        rate_limited_request(get_list_match_of_user, REGION, API_KEY, puuid)
        for puuid in puuids
    ]
    
    print(f"Total de joueurs : {len(list_of_matchIDs)}")
    print(f"Total de matche par joueur : {len(list_of_matchIDs[0])}\n")

    print("/============================/")
    print("/=== Création du fichier JSON stockant toutes les parties Diamond ===/")
    print("/============================/\n")

    start_time1 = time.time()

    # Boucle sur chaque joueur pour récupérer ses matchs
    for i, matchIDs in enumerate(list_of_matchIDs):
        print(f"-- Obtention des parties du joueur {i + 1} en cours... --")

        for matchID in matchIDs:
            rate_limited_request(create_and_add_json_element, "diamand.json", matchID, REGION, API_KEY)

        print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")

    end_time1 = time.time()

    # Affichage du temps d'exécution total
    print(f"Le temps d'exécution {Rank.DIAMOND.name} a pris : {end_time1 - start_time1:.2f} secondes")

    print("/=== PIPELINE DIAMOND TERMINÉ ===/")
    print("/=== FICHIER diamand.json ENREGISTRÉ ===/\n")
    
    
""" /=============================================================================/ """
""" /=============================================================================/ """
""" /=============================================================================/ """    
    
    

def pipeline() -> None:
    
    try:
        
        print("TEST")
        
        create_database()  # Crée la base de données si elle n'existe pas
        create_matches_table()  # Crée la table `matches` dans `lol_db`
        
        print("\nRécupération du JSON stockant le SUMMONER_ID\n")
        
        json_format_player = rate_limited_request(
            get_summoner_ID, TAGLINE, API_KEY, High_Rank.CHALLENGER.value, Queue_games.RANKED_SOLO.value
        )  
        
        print("\nParse le JSON et stock les SUMMONER_IDs dans une liste\n")
        
        summonerIDs = parse_json_summoner_ID(json_format_player)
        
        print("\nRécupération du PUUIDS de chaque joueur\n")
        
        puuids = [
            rate_limited_request(get_puuid_from_summoner_ID, TAGLINE, API_KEY, summonerID)
            for summonerID in summonerIDs
        ]
        
        print("\nRécupération d'une liste de X matchesIDs pour chaque PUUID\n")
        
        list_of_matchIDs = [
            rate_limited_request(get_list_match_of_user, REGION, API_KEY, puuid)
            for puuid in puuids
        ]
            
        print(f"Total de joueurs : {len(list_of_matchIDs)}")
        print(f"Total de matche par joueur : {len(list_of_matchIDs[0])}\n")
            
        start_time = time.time()
            
        for i in range(len(list_of_matchIDs)):
            print(f"-- Obtention des parties du joueur {i + 1} en cours... --")
                
            for matchID in list_of_matchIDs[i]:
                rate_limited_request(insert_data_into_db, matchID, High_Rank.CHALLENGER.name, get_matchs_details_from_match_ID_timeline(REGION, matchID, API_KEY))
                
            print(f"-- Obtention des parties du joueur {i + 1} terminé --\n")
                
        end_time = time.time()
            
        print(f"Le temps d'exécution {High_Rank.CHALLENGER.name} a pris : {end_time - start_time:.2f} secondes")
            
        
    except Exception as e:
        print(f"Erreur dans la pipeline: {e}")

if __name__ == "__main__":
    
    pipeline()