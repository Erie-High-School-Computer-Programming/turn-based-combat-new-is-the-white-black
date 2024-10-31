import random

class Player:
    def __init__(self, name, attack, defense, health_stat, move_list):
        """This method initializes the character
        It should give the character a name, attack, defense, and health stat
        It should also give the character a movelist"""
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health_stat = health_stat

        self.hp = 1000
        self.move_list = move_list
 
    def attack(self, move, target):
        """This method should allow the character to attack another character using the
        selected move. The move should deal damage to the target character"""

        if random.randint(0, 100) < self.move_list[move]["accuracy"]:
            target.hp -= self.move_list[move]["damage"]
            print(f"{target} was Hit")
        else:
            print("Attack missed lil bro")
    
    def display_stats(self):
        """This method should display the current health of the character"""
        print(self.name)
        print(self.hp)