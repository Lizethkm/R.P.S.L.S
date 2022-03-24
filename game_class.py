#  Gestures list, 

# functions: choose_gesture, Display_Greeting, display_rules, choose_game_type, compare_gestures, display_winner
import random
from ai_class import Ai
from human_class import Human

class Game:
    def __init__(self):
        self.ai_player = Ai()
        self.human_player = Human()

    def display_greeting(self):
        print('Welcome to R.P.S.L.S!!!!')
        print('This game dynamic is Rock,Paper,Scissors but with added fun.')
        print('Rule.1 No cheating\nRule.2 Best of 3 games' )
        

    def choose_game_type(self):
        # Will create a while loop to account for invalid entries. 
        # Working through the functions interactions first before executing
        game_choice = input('Type 1 for single player or Type 2 for multiplayer: ')
        if game_choice == '1':
            self.face_off_single_player()
        elif game_choice == '2':
            self.face_off_multiplayer()

        
    def face_off_single_player(self):
        # Created an instance to keep count of wins in the player class
        # while either player wins is less than 3 or human wins is less than 3, the while loop should continue 
        # if one equal 3 it should end the loop. I have not checked
        while self.ai_player.wins < 3 or self.human_player.wins < 3:
            self.human_player.choose_gesture()
            user_gesture_index = int(input('Pick a gesture: '))
            self.user_choice = self.human_player.gestures_list[user_gesture_index]
            self.ai_choice = self.ai_player.choose_gesture()
            print(f"The computer's choice is: {self.ai_choice}")

            self.compare_gestures_single_player()
            if self.ai_player.wins == 3:
                self.display_winner("Computer")
            elif self.human_player.wins == 3:
                self.display_winner("You")

    def face_off_multiplayer(self):
        # players for two humans. Hypethical
        self.choose_gesture()
        player_one= int(input('Player one pick a gesture: '))
        self.choose_gesture()
        player_two= int(input('Player two pick a gesture: '))


    def run_game(self):
        self.display_greeting()
        self.choose_game_type()

    def compare_gestures_single_player(self):
        if self.user_choice == self.ai_choice:
            print("You have a draw for this round")
        # Each gesture can defend two other gestures. Making a universal if statement for each gesture
        # If scissors wins for either human or ai
        if self.user_choice == self.human_player.gestures_list[0] and self.ai_choice == self.ai_player.gestures_list[2] or self.ai_choice == self.ai_player.gestures_list[3]:
            print(f"{self.human_player.gestures_list[0]} takes the cake! You win this round!")
            self.human_player.wins += 1

        elif self.ai_choice == self.ai_player.gestures_list[0] and self.user_choice == self.human_player.gestures_list[2] or self.user_choice == self.human_player.gestures_list[3]:
            print(f"The computer wins this round sorry!")
            self.ai_player.wins += 1

        # if spock wins for either human or ai
        if self.user_choice == self.human_player.gestures_list[1] and self.ai_choice == self.ai_player.gestures_list[0] or self.ai_choice == self.ai_player.gestures_list[4]:
            print(f"{self.human_player.gestures_list[1]} ventures to beat this round!")
            self.human_player.wins += 1

        elif self.ai_choice == self.ai_player.gestures_list[1] and self.user_choice == self.human_player.gestures_list[0] or self.user_choice == self.human_player.gestures_list[4]:
            print(f"Computer chose {self.ai_player.gestures_list[1]}  correctly. You lose this round")
            self.ai_player.wins += 1

        # if paper wins for either side
        if self.user_choice == self.human_player.gestures_list[2] and self.ai_choice == self.ai_player.gestures_list[4] or self.ai_choice == self.ai_player.gestures_list[1]:
            print(f"{self.human_player.gestures_list[2]} wins!")
            self.human_player.wins += 1

        elif self.ai_choice == self.ai_player.gestures_list[2] and self.user_choice == self.human_player.gestures_list[1] or self.user_choice == self.human_player.gestures_list[4]:
            print(f"Computer chose {self.ai_player.gestures_list[2]} wins this time. ")
            self.ai_player.wins += 1

        # if lizard wins 
        if self.user_choice == self.human_player.gestures_list[3] and self.ai_choice == self.ai_player.gestures_list[1] or self.ai_choice == self.ai_player.gestures_list[2]:
            print(f" You chose right! {self.human_player.gestures_list[3]} wins! ")
            self.human_player.wins += 1

        elif self.ai_choice == self.ai_player.gestures_list[3] and self.user_choice == self.human_player.gestures_list[1] or self.user_choice == self.human_player.gestures_list[2]:
            print(f"Computers wins this round with {self.ai_player.gestures_list[3]}")
            self.ai_player.wins += 1

        # if rock wins 
        if self.user_choice == self.human_player.gestures_list[4] and self.ai_choice == self.ai_player.gestures_list[0] or self.ai_choice == self.ai_player.gestures_list[3]:
            print(f"You win this round with {self.human_player.gestures_list[4]}!")
            self.human_player.wins += 1 
        
        elif self.ai_choice == self.ai_player.gestures_list[4] and self.user_choice == self.human_player.gestures_list[0] or self.user_choice == self.human_player.gestures_list[3]:
            print(f"Computers wins with the {self.ai_player.gestures_list[4]} choice. You lose")
            self.ai_player.wins += 1

    def compare_gestures_multiplayer(self):
        pass

    def display_winner(self,winner):
        print(f"{winner} has one the game")
        # just theory for now. We can change. My thoughts were to help it work with the for loop for when we run the game

game = Game()
game.face_off_single_player()
