import sys
import random

class Player:
    def __init__(self, name, move_list, health):
        self.name = name
        self.move_list = move_list
        self.health = health

    def attack(self, opponent, move_name):
        move = self.move_list[move_name]
        if random.randint(1, 100) <= move["accuracy"]:
            opponent.health -= move["damage"]
            print(f"{self.name} attacks {opponent.name} with {move_name} for {move['damage']} damage!")
        else:
            print(f"{self.name}'s attack with {move_name} missed!")

class Game:
    def __init__(self):
        print("Hello and welcome to the game!")
        self.puppaydog = Player("Puppay", {
            "Puppay": {"damage": 150, "accuracy": 50},
            "Tornadotwisty": {"damage": 350, "accuracy": 35},
            "PuppayDog Eyes": {"damage": 50, "accuracy": 90}, 
        }, 1000)

        self.kittaycat = Player("Kittay", {
            "cat": {"damage": 130, "accuracy": 65},
            "The-wip": {"damage": 370, "accuracy": 35},
            "kungfu": {"damage": 75, "accuracy": 80}
        }, 1000)

        self.select_characters()
        self.player_turn = random.choice([True, False])

    def select_characters(self):
        choosing = True
        while choosing:
            choice = input("Which player would you like to be? Puppay (a) or Kittay (b) >> ")
            if choice == "a":
                self.player = self.puppaydog
                self.computer = self.kittaycat
                choosing = False
            elif choice == "b":
                self.player = self.kittaycat
                self.computer = self.puppaydog
                choosing = False
            else:
                print("Invalid response. Please pick a or b.")

    def turn(self):
        print(f"\nCurrent Health: {self.player.name}: {self.player.health}, {self.computer.name}: {self.computer.health}")
        
        if self.player_turn:
            move = input(f"{self.player.name}, pick your attack: {', '.join(self.player.move_list.keys())} >> ")
            if move in self.player.move_list:
                self.player.attack(self.computer, move)
            else:
                print("Invalid move. Please try again.")
                return
        else:
            move = random.choice(list(self.computer.move_list.keys()))
            self.computer.attack(self.player, move)

        self.player_turn = not self.player_turn

    def check_winner(self):
        if self.player.health <= 0:
            print(f"{self.computer.name} wins!")
            return True
        elif self.computer.health <= 0:
            print(f"{self.player.name} wins!")
            return True
        return False

    def exit(self):
        print("Thanks for playing!")
        sys.exit()

    def run(self):
        while True:
            self.turn()
            if self.check_winner():
                restart = input("Do you want to play again? (y/n) >> ")
                if restart.lower() == 'y':
                    self.__init__()  # Restart the game
                else:
                    self.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()