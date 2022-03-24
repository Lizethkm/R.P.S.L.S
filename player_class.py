#Player name, 

from tkinter.font import nametofont


class Player:
    def __init__(self):
        self.wins = 0
        # Where we can have a default choose gesture method
        # when ai inherits player the method can change to random
        # when human inferits player the method can be default
        self.gestures_list = ['Scissors', 'Spock','Paper','Lizards','Rock']
    
    def choose_gesture(self):
        index = 0
        for gestures in self.gestures_list:
            print(f" Type {index} for {gestures}")
            index += 1

        


