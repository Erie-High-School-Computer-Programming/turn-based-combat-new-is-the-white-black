class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hp = 100

    def birthday(self):
        self.age += 1

    def attack(self, target):
        target.hp -= 10

luna = Dog("Luna", 4)
print(luna.age) 
luna.birthday()
print(luna.age)

pikachu = Dog("Pikachu", 2)

print(pikachu.hp)
luna.attack(pikachu)
print(pikachu.hp)

move_list = {"bite": {"damage": 10, 
                    "accuracy": 50},
                    "scratch": 5, 
                    "lick": 1}
import random
if random.randint(0, 100) < move_list["bite"]["accuracy"]:
    pikachu.hp -= move_list["bite"]["damage"]
    print("Pikachu was bitten")
else: 
    print("Attack missed")