import json
import random

from typing import Any, Dict, List


def parse_json_summoner_ID(json_format_player: List[Dict[str, Any]]) -> List[str]:
    
    result_list = []
    entries_size = len(json_format_player.get("entries"))
    
    for i in range(entries_size - 1):
        result_list.append(json_format_player['entries'][i]['summonerId'])
        
    return random.sample(result_list, 8)


def parse_json_summoner_ID_low_elo(json_format_player: List[Dict[str, Any]]) -> List[str]:
    
    result_list = []
    
    for i in range(len(json_format_player)):
        result_list.append(json_format_player[i]['summonerId'])
        
    return result_list