from game_files.entities import *
from game_files.managers import *
import random, os
from time import sleep



def game_setup():
    nome = input("Warrior name: ")
    plr = Player(name=nome, health=100.0, attack=5, defense=2)
    return plr

plr = game_setup()
game_manager=GameManager(plr)
os.system('clear||cls')


game_manager.start()

print('\n')
input("Press any key to exit...")
