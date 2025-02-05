import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement sur lol
API_KEY = os.getenv("API_KEY")
REGION = os.getenv("REGION")
RIOT_ID = os.getenv("RIOT_ID")
TAGLINE = os.getenv("TAGLINE")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

# Assurez-vous de vérifier si les variables sont chargées correctement
if not all(
    
    [API_KEY, REGION, RIOT_ID, TAGLINE, DB_CONFIG]
    
    ):
    
    raise ValueError("Certaines variables d'environnement manquent dans .env")