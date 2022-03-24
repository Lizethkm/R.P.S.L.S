# Name, 

from player_class import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def change_name(self):
        # Changes the name for the user. 
        # Ava is still hardcored for the AI's name but can be changed with this function
        # I have tested
        name = input("Name your player: ")
        self.name = name


