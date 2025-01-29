import json

def main() -> None:
    
    with open("../../data/raw/challenger_games.json", 'r') as f:
        data = json.load(f)
        
    print(f"La taille du fichier est de : {len(data)}")

if __name__ == "__main__":
    
    main()