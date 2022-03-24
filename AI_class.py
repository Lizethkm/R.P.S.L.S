
from player_class import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()

    
    def choose_gesture(self):
            ai_gesture= random.choice(self.gestures_list)
            return ai_gesture
