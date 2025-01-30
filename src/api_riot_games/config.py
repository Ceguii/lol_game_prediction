import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement
API_KEY = os.getenv("API_KEY")
REGION = os.getenv("REGION")
RIOT_ID = os.getenv("RIOT_ID")
TAGLINE = os.getenv("TAGLINE")

# Assurez-vous de vérifier si les variables sont chargées correctement
if not all([API_KEY, REGION, RIOT_ID, TAGLINE]):
    raise ValueError("Certaines variables d'environnement manquent dans .env")