from enum import Enum

class High_Rank(Enum):
    
    CHALLENGER = "challengerleagues"
    GRAND_MASTER = "grandmasterleagues"
    MASTER = "masterleagues"
    
class Rank(Enum):

    DIAMOND = "DIAMOND"
    PLATINUM = "PLATINUM"
    GOLD = "GOLD"
    SILVER = "SILVER"
    BRONZE = "BRONZE"
    IRON = "IRON"
    
class Queue_games(Enum):
    
    RANKED_SOLO = "RANKED_SOLO_5x5"
    RANKED_FLEX = "RANKED_FLEX_SR"
    RANKED_FLEX_T = "RANKED_FLEX_TT"
    