import os
import sys
import time
import requests


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