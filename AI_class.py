#  Hardcode name, 
# Randomly select gesture
# don't need to enter player's name if we import player parent class. 
# You provide name as an instance in player
from player_class import Player


class Ai(Player):
    def __init__(self):
        super().__init__()