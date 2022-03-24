# STEPS FOR THE ROCK PAPER SCISSORS SPOCK 
# STEPS:  
# Display a welcome [Game Class] 
# Display rules for the game [Game Class] 
# Single player game or a Multiplayer game?  user input [Game Class] 
# Choose who goes first 
# Display the gesture choices for player class  
# Self.gestures = [“rock”, “paper”, “scissors”, “lizard”, “spock”] 
# For the first player chooses a gesture  
# Player two chooses a gesture  
# Compare the inputs for the 2 players and declare which one is wins based on the rules  
# Keep track of wins or score 
# Repeat steps 4 through 8  
# Whoever gets best of 3 games (full three rounds) first is the winner 
# Display winner  
# CLASSES:  
# Player [Parent Class] 
# Game 
# Human [Child to player] 
# AI [Child to player] 
from game_class import Game
game = Game()
game.run_game()