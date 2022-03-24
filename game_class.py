#  Gestures list, 

# functions: choose_gesture, Display_Greeting, display_rules, choose_game_type, compare_gestures, display_winner
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
        # Will create a while loop to account for invalid entries. 
        # Working through the functions interactions first before executing
        game_choice = input('Type 1 for single player or Type 2 for multiplayer: ')
        if game_choice == '1':
            self.face_off_single_player()

        elif game_choice == '2':
            self.player_two= Human()
            self.face_off_single_player() #if works change function face_off name

        
    def face_off_single_player(self):
        # Created an instance to keep count of wins in the player class
        # while either player wins is less than 3 or human wins is less than 3, the while loop should continue 
        # if one equal 3 it should end the loop. I have not checked
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one_choice = self.player_one.choose_gesture()
            # self.user_choice = self.human_player.gestures_list[user_gesture_index]
            self.player_two_choice = self.player_two.choose_gesture()
            print(f"The computer's choice is: {self.player_two_choice}")

            self.compare_gestures_single_player()
            if self.player_two.wins >= 2:
                self.display_winner("Player 2") 
            elif self.player_one.wins >= 2:
                self.display_winner("You")

    def run_game(self):
        self.display_greeting()
        self.choose_game_type()

    def compare_gestures_single_player(self):
        if self.player_one_choice == self.player_two_choice:
            print("You have a draw for this round")
        # Each gesture can defend two other gestures. Making a universal if statement for each gesture
        # If scissors wins for either human or ai
        if self.player_one_choice == self.player_one.gestures_list[0] and (self.player_two_choice == self.player_two.gestures_list[2] or self.player_two_choice == self.player_two.gestures_list[3]):
            print(f"{self.player_one_choice} takes the cake! You win this round!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[0] and (self.player_one_choice == self.player_one_choice.gestures_list[2] or self.player_one_choice == self.player_one_choice.gestures_list[3]):
            print(f"The {self.player_two_choice} wins this round sorry!")
            self.player_two.wins += 1

        # if spock wins for either human or ai
        if self.player_one_choice == self.player_one.gestures_list[1] and (self.player_two_choice == self.player_two.gestures_list[0] or self.player_two_choice == self.player_two.gestures_list[4]):
            print(f"{self.player_one_choice} ventures to beat this round!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[1] and (self.player_one_choice == self.player_one.gestures_list[0] or self.player_one_choice == self.player_one.gestures_list[4]):
            print(f"Player Two chose {self.player_two_choice}  correctly. You lose this round")
            self.player_two.wins += 1

        # if paper wins for either side
        if self.player_one_choice == self.player_one.gestures_list[2] and (self.player_two_choice == self.player_two.gestures_list[4] or self.player_two_choice == self.player_two.gestures_list[1]):
            print(f"{self.player_one_choice} wins!")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[2] and (self.player_one_choice == self.player_one.gestures_list[1] or self.player_one_choice == self.player_one.gestures_list[4]):
            print(f"Player Two chose {self.player_two_choice} wins this time. ")
            self.player_two.wins += 1

        # if lizard wins 
        if self.player_one_choice == self.player_one.gestures_list[3] and (self.player_two_choice == self.player_two.gestures_list[1] or self.player_two_choice == self.player_two.gestures_list[2]):
            print(f" You chose right! {self.player_one_choice} wins! ")
            self.player_one.wins += 1

        elif self.player_two_choice == self.player_two.gestures_list[3] and (self.player_one_choice == self.player_one.gestures_list[1] or self.player_one_choice == self.player_one.gestures_list[2]):
            print(f"Player Two wins this round with {self.player_two_choice}")
            self.player_two.wins += 1

        # if rock wins 
        if self.player_one_choice == self.player_one.gestures_list[4] and (self.player_two_choice == self.player_two.gestures_list[0] or self.player_two_choice == self.player_two.gestures_list[3]):
            print(f"You win this round with {self.player_one_choice}!")
            self.player_one.wins += 1 
        
        elif self.player_two_choice == self.player_two.gestures_list[4] and (self.player_one_choice == self.player_one.gestures_list[0] or self.player_one_choice == self.player_one.gestures_list[3]):
            print(f"Player Two wins with the {self.player_two_choice} choice. You lose")
            self.player_two.wins += 1


    def display_winner(self,winner):
        print(f"{winner} has won the game")
        # just theory for now. We can change. My thoughts were to help it work with the for loop for when we run the game

game = Game()
game.run_game()
