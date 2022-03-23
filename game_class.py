#  Gestures list, 

# functions: choose_gesture, Display_Greeting, display_rules, choose_game_type, compare_gestures, display_winner
import random

class Game:
    def __init__(self):
        self.gestures_list= ['Scissors', 'Spock','Paper','Lizards','Rock']


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
        
        
    def random_ai_gesture(self):
        #runs for the ai's turn to play
        ai_gesture= random.choice(self.gestures_list)
        return ai_gesture
        
    def face_off_single_player(self):
        #while loop to face off between ai & player
        self.choose_gesture()  
        # Made pick_gesture into an integer because we will use that number later
        pick_gesture = int(input('Pick a gesture: ')) #for the while loop
        ai_choice = self.random_ai_gesture()
        print(f"The computer's choice is: {ai_choice}")
        # created a full sentence for the ai choice ^ also tested

    def face_off_multiplayer(self):
        # players for two humans. Hypethical
        self.choose_gesture()
        player_one= int(input('Player one pick a gesture: '))
        self.choose_gesture()
        player_two= int(input('Player two pick a gesture: '))


    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.choose_game_type()

        

    def compare_gestures(self):
        self.choose_gesture()

    def display_winner(self,winner):
        print(f"{winner} has one the game")
        # just theory for now. We can change. My thoughts were to help it work with the for loop for when we run the game
