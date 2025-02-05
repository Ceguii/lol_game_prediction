from typing import Any, Dict
import psycopg2
from psycopg2 import sql
import os
from config import DB_CONFIG


def create_database() -> None:
    """Crée la base de données 'lol_db' si elle n'existe pas."""
    conn = None
    try:
        # Connexion à PostgreSQL avec le mot de passe
        conn = psycopg2.connect(**DB_CONFIG, database="postgres")  
        conn.autocommit = True  # Permet la création de la base

        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'lol_db';")
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("lol_db")))
            print("Base de données 'lol_db' créée avec succès !")
        else:
            print("La base de données 'lol_db' existe déjà.")

        cursor.close()
    except Exception as e:
        print(f"Erreur lors de la création de la base de données : {e}")
    finally:
        if conn:
            conn.close()

def create_matches_table() -> None:
    """Crée la table 'matches' dans la base de données 'lol_db'."""
    conn = None
    try:
        # Connexion à `lol_db`
        conn = psycopg2.connect(**DB_CONFIG, database="lol_db")  
        cursor = conn.cursor()

        # Création de la table `matches`
        create_table_query = """
        CREATE TABLE IF NOT EXISTS matches (
            match_id TEXT PRIMARY KEY,
            rank TEXT,
            json_data JSONB
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'matches' créée avec succès !")

        cursor.close()
    except Exception as e:
        print(f"Erreur lors de la création de la table : {e}")
    finally:
        if conn:
            conn.close()
            
def insert_data_into_db(match_id, rank, json_data) -> None:
    """Insère les données dans la table 'matches'."""
    conn = None
    try:
        # Connexion à `lol_db`
        conn = psycopg2.connect(**DB_CONFIG, database="lol_db")  
        cursor = conn.cursor()

        # Préparer la requête d'insertion
        insert_query = """
        INSERT INTO matches (match_id, rank, json_data) 
        VALUES (%s, %s, %s)
        ON CONFLICT (match_id) DO NOTHING;  -- Si le match_id existe déjà, ne rien faire.
        """
        
        # Exécuter la requête d'insertion avec les valeurs fournies
        cursor.execute(insert_query, (match_id, rank, json_data))
        conn.commit()
        print(f"Données insérées pour le match {match_id} avec succès !")

        cursor.close()
    except Exception as e:
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    
    create_database()  # Crée la base de données si elle n'existe pas
    create_matches_table()  # Crée la table `matches` dans `lol_db`



    # Exemple 1 : Insérer un match avec des données JSON simples
    match_id_1 = "match_001"
    rank_1 = "Gold"
    json_data_1 = {
        "player1": {"name": "Player1", "champion": "Ahri", "kills": 10},
        "player2": {"name": "Player2", "champion": "Zed", "kills": 8}
    }
    insert_data_into_db(match_id_1, rank_1, json_data_1)

    # Exemple 2 : Insérer un autre match avec des données JSON plus complexes
    match_id_2 = "match_002"
    rank_2 = "Platinum"
    json_data_2 = {
        "player1": {"name": "Player1", "champion": "Lux", "kills": 12, "deaths": 2},
        "player2": {"name": "Player2", "champion": "Riven", "kills": 7, "deaths": 3},
        "player3": {"name": "Player3", "champion": "Jhin", "kills": 15, "deaths": 0}
    }
    insert_data_into_db(match_id_2, rank_2, json_data_2)

    # Exemple 3 : Insérer un match avec des données plus simples
    match_id_3 = "match_003"
    rank_3 = "Silver"
    json_data_3 = {
        "player1": {"name": "Player1", "champion": "Teemo", "kills": 5},
        "player2": {"name": "Player2", "champion": "Yasuo", "kills": 9}
    }
    insert_data_into_db(match_id_3, rank_3, json_data_3)