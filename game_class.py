
import random
from ai_class import Ai
from human_class import Human

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two= Ai()

    def display_greeting(self):
        print('Welcome to R.P.S.L.S!!!!')
        print('This game dynamic is Rock,Paper,Scissors but with added fun.')
        print('Rule.1 No cheating\nRule.2 Best of 3 games' )
        

    def choose_game_type(self):
        while True:
            game_choice = int(input('Type 1 for single player or Type 2 for multiplayer: '))
            if game_choice not in [1,2]:
                continue
            else: 
                break

        if game_choice == 1:
            self.face_off()

        elif game_choice == 2:
            self.player_two= Human()
            self.face_off() 

        
    def face_off(self):
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one_choice = self.player_one.choose_gesture()
            self.player_two_choice = self.player_two.choose_gesture()
            print(f"Player Two's choice is: {self.player_two_choice}")

            self.compare_gestures()
            if self.player_two.wins >= 2:
                self.display_winner("Player Two") 
            elif self.player_one.wins >= 2:
                self.display_winner("Player One")

    def run_game(self):
        self.display_greeting()
        self.choose_game_type()

    def compare_gestures(self):
        if self.player_one_choice == self.player_two_choice:
            print("You have a draw for this round")
        # If scissors wins for either human or ai
        if self.player_one_choice == self.player_one.gestures_list[0] and (self.player_two_choice == self.player_two.gestures_list[2] or self.player_two_choice == self.player_two.gestures_list[3]):
            print(f"{self.player_one_choice} takes the cake! You win this round!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[0] and (self.player_one_choice == self.player_one.gestures_list[2] or self.player_one_choice == self.player_one.gestures_list[3]):
            print(f"{self.player_one_choice} doesn't cut it, sorry! Player Two wins this round!!")
            self.player_two.wins += 1

        # if spock wins for either human or ai
        if self.player_one_choice == self.player_one.gestures_list[1] and (self.player_two_choice == self.player_two.gestures_list[0] or self.player_two_choice == self.player_two.gestures_list[4]):
            print(f"{self.player_one_choice} ventures to beat this round!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[1] and (self.player_one_choice == self.player_one.gestures_list[0] or self.player_one_choice == self.player_one.gestures_list[4]):
            print(f"{self.player_two_choice}  mind melded this round. You lose!")
            self.player_two.wins += 1

        # if paper wins for either side
        if self.player_one_choice == self.player_one.gestures_list[2] and (self.player_two_choice == self.player_two.gestures_list[4] or self.player_two_choice == self.player_two.gestures_list[1]):
            print(f"{self.player_one_choice} hole punched {self.player_two_choice}, you win this round!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[2] and (self.player_one_choice == self.player_one.gestures_list[1] or self.player_one_choice == self.player_one.gestures_list[4]):
            print(f"{self.player_two_choice} recyled you. Player Two wins this round! ")
            self.player_two.wins += 1

        # if lizard wins 
        if self.player_one_choice == self.player_one.gestures_list[3] and (self.player_two_choice == self.player_two.gestures_list[1] or self.player_two_choice == self.player_two.gestures_list[2]):
            print(f"{self.player_one_choice} had it from the gec-ko, you win this round! ")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[3] and (self.player_one_choice == self.player_one.gestures_list[1] or self.player_one_choice == self.player_one.gestures_list[2]):
            print(f"Player Two is off to see the {self.player_two_choice} of Oz, you lose!")
            self.player_two.wins += 1

        # if rock wins 
        if self.player_one_choice == self.player_one.gestures_list[4] and (self.player_two_choice == self.player_two.gestures_list[0] or self.player_two_choice == self.player_two.gestures_list[3]):
            print(f"You {self.player_one_choice}, you win this round!")
            self.player_one.wins += 1 
        
        elif self.player_two_choice == self.player_two.gestures_list[4] and (self.player_one_choice == self.player_one.gestures_list[0] or self.player_one_choice == self.player_one.gestures_list[3]):
            print(f"Can you smell what the {self.player_two_choice} is cooking? It's you! You lose!")
            self.player_two.wins += 1


    def display_winner(self,winner):
        print(f"{winner} has won the game")
    


