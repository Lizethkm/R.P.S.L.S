#  Hardcode name, 
# Randomly select gesture
# don't need to enter player's name if we import player parent class. 
# You provide name as an instance in player
from player_class import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    # tested and works. Randomizes the ai choice of gesture
    def choose_gesture(self):
        ai_gesture= random.choice(self.gestures_list)
        return ai_gesture
