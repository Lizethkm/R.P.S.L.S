#  Gestures list, 

# functions: choose_gesture, Display_Greeting, display_rules, choose_game_type, compare_gestures, display_winner
import random

class Game:
    def __init__(self):
        self.gestures_list= ['Scissors', 'Spock','Paper','Lizards','Rock']


    def display_greeting(self):
        print('Welcome to R.P.S.L.S!!!!')

    def display_rules(self):
        print('This game dynamic is Rock,Paper,Scissors but with added fun.')
        print('Rule.1- No cheating + \n + Rule.2 Best of 3 games' )

    def choose_game_type(self):
        game_choice=input('Press 1 for single player or Press 2 for multiplayer: ')
        if game_choice == '1':
            pass
        elif game_choice == '2':
            pass
        else:
            print('Choose invalid')
            game_choice=input('Press 1 for single player or Press 2 for multiplayer: ') #don't forget to make the loop


    def choose_gesture(self):
        index = 0
        for gestures in self.gestures_list:
            print(f" Type {index} for {gestures}")
            index += 1
        
        

    def random_ai_gesture(self):
        #if ai turn 
        ai_gesture= random.choice(self.gestures_list)
        return ai_gesture
        
    def face_off_single_player(self):
        self.choose_gesture()#while loop to face off between ai & player 
        pick_gesture= input('Pick a gesture: ') #for the while loop
        print(self.random_ai_gesture())

    def face_off_multiplayer(self):
        self.choose_gesture()
        player_one= int(input('Player one pick a gesture: '))
        self.choose_gesture()
        player_two= int(input('Player two pick a gesture: '))


    def run_game(self):
        self.display_greeting()
        self.display_rules()

        

    def compare_gestures(self):
        self.choose_gesture()


# print(Winner)
game = Game()
game.face_off_multiplayer()