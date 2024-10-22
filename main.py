import pygame
# Create a game that allows players to choose between multiple characters
# and fight against each other. The game should have a simple combat system
# where characters can deal damage to each other. The game should also have
# a way to display the current health of each character.

# The game should have turned based combat where each player takes turns
# Players should have an attack, defense, and health stat

# Combat should involve a level of randomness.

# The game should have a way to display the current health of each character after each turn.

# Combat should continue until one of the characters health reaches 0.

# The game should have a way to display the winner of the game.

# The game should have a way to restart the game.

# The game should have a way to exit the game.
import sys
from player import Player

class Game:
    def __init__(self, name, strength):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        print("Hello and welcome")
        
        self.name = name
        self.strength = strength
        self.hp = 100

        self.player_turn = True # False will mean the computers turn
        #print(self.current_turn)

    def turn(self, current_turn):
        """This method should show the current health of both players, 
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        self.player_turn = not self.player_turn

    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        if player.health <= 0:
            check_winner()

    def restart(self):
        """This method should allow the player to restart the game"""
        

    def exit(self):
        """This method should allow the player to exit the game"""
        sys.exit()

puppaydog = Game("Puppay", 1203)

    
def main():
    game = Game()
    game.turn(1)
    game.check_winner()
    game.turn(2)
    game.check_winner()

#This calls the main function
main()