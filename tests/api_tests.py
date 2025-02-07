import sys
import os 
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


# Maintenant, tu peux importer ta fonction depuis src/api_riot_games/api_fetcher/parse_json
from api_riot_games.api_fetcher.parse_json import parse_json_summoner_ID_low_elo
from api_riot_games.api_fetcher.api_data_fetcher import get_summoner_ID_low_elo, get_puuid_from_summoner_ID

""" 


blueTeamWin	
blueTeamWardsPlaced	
blueTeamWardsDestroyed	
blueTeamFirstBlood	
blueTeamKills	
blueTeamDeaths	
blueTeamAssists	
blueTeamDragons	
blueTeamHeralds	
blueTeamTowerDestroyed	
blueTeamTotalGold	
blueTeamAvgLevel	
blueTeamTotalMinionsKilled	
blueTeamTotalJungleMonsterKilled	
blueTeamCsPerMinute	
blueTeamGoldPerMinute	
gameDuration (in seconds)

CREATE TABLE match_results (
    match_id SERIAL PRIMARY KEY,
    game_duration INTEGER,  -- durée du match en secondes
    blue_team_win INTEGER,  -- 1 si l'équipe bleue a gagné, 0 sinon
    red_team_win INTEGER    -- 1 si l'équipe rouge a gagné, 0 sinon
);

CREATE TABLE team_stats (
    match_id INTEGER REFERENCES match_results(match_id),
    team_id INTEGER,  -- 100 pour l'équipe bleue, 200 pour l'équipe rouge
    wards_placed FLOAT,
    wards_destroyed FLOAT,
    first_blood INTEGER,  -- 1 si l'équipe a tué le premier champion, 0 sinon
    kills INTEGER,
    deaths INTEGER,
    assists INTEGER,
    dragons INTEGER,
    heralds INTEGER,
    tower_destroyed INTEGER,
    total_gold INTEGER,
    avg_level FLOAT,
    total_minions_killed INTEGER,
    total_jungle_monster_killed INTEGER,
    cs_per_minute FLOAT,
    gold_per_minute FLOAT,
    PRIMARY KEY (match_id, team_id)
);

"""


def extract_data_ward_placed(file_name):
    
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    blue_team = 0
    red_team = 0
    
    for frame in data['info']['frames']:
        for event in frame['events']:
            
            if event['type'] == "PAUSE_END":
                continue
           
            if event['type'] == "WARD_PLACED" and 'creatorId' in event:
               
                if event['creatorId'] <= 5:
                    blue_team += 1
                else:
                    red_team += 1
                    
    return blue_team, red_team


if __name__ == '__main__':
    
    blue, red = extract_data_ward_placed("test.json")
    
    print(blue)
    print(red)