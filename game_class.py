#  Gestures list, 

# functions: choose_gesture, Display_Greeting, display_rules, choose_game_type, compare_gestures, display_winner
import random
from ai_class import Ai
from human_class import Human

class Game:
    def __init__(self):
        self.gestures_list= ['Scissors', 'Spock','Paper','Lizards','Rock']
        self.ai_player = Ai()
        self.human_player = Human()

    def display_greeting(self):
        print('Welcome to R.P.S.L.S!!!!')
        print('This game dynamic is Rock,Paper,Scissors but with added fun.')
        print('Rule.1 No cheating\nRule.2 Best of 3 games' )
        # deleted the rules methods and added the statements to greeting. 
        # added the actual rules and logic to the README.md

    def choose_game_type(self):
        # Will create a while loop to account for invalid entries. 
        # Once the user select one or two the loop should stop
        # Working through the functions interactions first before executing
        game_choice = input('Type 1 for single player or Type 2 for multiplayer: ')
        if game_choice == '1':
            #if the answer is one, it will call the single player game.
            self.face_off_single_player()
        elif game_choice == '2':
            # is the answer is two, it will call the single player game.
            self.face_off_multiplayer()

    def choose_gesture(self):
        index = 0
        for gestures in self.gestures_list:
            print(f" Type {index} for {gestures}")
            index += 1
        
    # move to player class as a default method and change to this is ai class
    def random_ai_gesture(self):
        #runs for the ai's turn to play
        ai_gesture= random.choice(self.gestures_list)
        return ai_gesture
        
    def face_off_single_player(self):
        # Created an instance to keep count of wins in the player class
        # while either player wins is less than 3 or human wins is less than 3, the while loop should continue 
        # if one equal 3 it should end the loop. I have not checked
        while self.ai_player.wins < 3 or self.human_player.wins < 3:
            self.choose_gesture()
            user_gesture_index = int(input('Pick a gesture: '))
            self.user_choice = self.gestures_list[user_gesture_index]
            self.ai_choice = self.random_ai_gesture()
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
            self.ai_player.wins += 1
            self.human_player.wins += 1
        # Human choice is Scissors and Computer choice is either Paper or Lizard
        # final elif covers if ai wins 
        if self.user_choice == self.gestures_list[0] and self.ai_choice == self.gestures_list[2]:
            print(f"{self.gestures_list[0]} cuts {self.gestures_list[2]}! You win this round!")
         # adds a win to the player wins for human
            self.human_player.wins += 1
        elif self.user_choice == self.gestures_list[0] and self.ai_choice == self.gestures_list[3]:
            print(f"{self.gestures_list[0]} decapitates {self.gestures_list[3]}! You win this round!")
            self.human_player.wins += 1
        elif self.ai_choice == self.gestures_list[0] and self.user_choice == self.gestures_list[2] or self.gestures_list[3]:
            print(f"The computer wins this round sorry!")
            self.ai_player.wins += 1

    def compare_gestures_multiplayer(self):
        pass

    def display_winner(self,winner):
        print(f"{winner} has one the game")
        # just theory for now. We can change. My thoughts were to help it work with the for loop for when we run the game
