
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
import random
from player import Player
 
class Game:
    def __init__(self):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        print("Hello and welcome")
        self.puppaydog = Player("Puppay", "Tornadotwisty", "PuppayDog Eyes", 1000, move_list =
        {
            "Puppay": {"damage": 150, "accuracy": 50},
            "Tornadotwisty": {"damage": 350, "accuracy": 20},
            "PuppayDog Eyes": {"damage": 50, "accuracy": 90}
        })
        self.kittaycat = Player("cat", "the-wip", "kungfu", 1000, move_list =
        {
            "cat": {"damage": 130, "accuracy": 65 },
            "The-wip": {"damage": 370, "accuracy": 7},
            "kungfu": {"damage": 75, "accuracy": 80}
        })
 
        choosing = True
        while choosing:
            choice = input("Which player would you like to be? puppaydog (a) or kittaycat (b) >>")
            if choice == "a":
                self.player = self.puppaydog
                choosing = False
            elif choice == "b": 
                self.player = self.kittaycat
                choosing = False
            else: 
                print("Invalid response. Please pick a or b.")

        self.player_turn = random.choice([True, False]) # True will means it's your turn, False will mean the computers turn.
        self.computer = self.kittaycat if self.player == self.puppaydog else self.puppaydog

    def turn(self):
        """This method should show the current health of both players,
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        print(f"{self.player.name}'s health: {self.player.hp} | {self.computer.name}'s health: {self.computer.hp}")
        if self.player_turn:
            if self.player == self.puppaydog: 
                move = input("Pick your attack: Puppay (a), Tornadotwisty (b), or PuppayDog Eyes (c) >> ")
                if move == "a":
                    move_name = "Puppay"
                elif move == "b":
                    move_name = "Tornadotwisty"
                elif move == "c":
                    move_name = "PuppayDog Eyes"
                elif move == "quit":
                    self.exit()
                else:
                    print("Invalid move. Try again.")
                    return
                self.attack(self.player, self.computer, move_name)
            else:
                move_name = random.choice(list(self.computer.move_list.keys()))
                self.attack(self.computer, self.player, move_name)

            self.player_turn = not self.player_turn

    def attack(self, attacker, defender, move_name):
        move = attacker.move_list[move_name]
        damage = move["damage"]
        accuracy = move["accuracy"]

        if random.randint(1, 100) <= accuracy:
            defender.hp -= damage
            print(f"{attacker.name} attacks {defender.name} with {move_name} for {damage} damage!")
        else:
            print(f"{attacker.name}'s attack missed")

 
    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        if self.player.hp <= 0: 
            print(f"{self.computer.name} ROCKED YO SHI")
            self.playing = False
        elif self.computer.hp <= 0: 
            print(f"{self.player.name} got lucky")
            self.playing = False
 
    def exit(self):
        """This method should allow the player to exit the game"""
        sys.exit()
 
 
    def run(self):
        self.playing = True
        while self.playing:
            self.turn()
            self.check_winner()
       
def main():
    game = Game()
    game.run()
 
main()