from game_files.entities import *
from game_files.enemy_table import enemies
from game_files.event_manager import EventManager
import random, os
from time import sleep



def game_setup():
    nome = input("Warrior name: ")
    plr = Player(name=nome, health=100.0, attack=5, defense=2)
    return plr

plr = game_setup()
plr_manager=EventManager(plr)
os.system('clear||cls')


plr_manager.start()

print('\n')
input("Press any key to exit...")
