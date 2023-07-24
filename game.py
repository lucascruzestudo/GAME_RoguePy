from game_files.entities import *
from game_files.manager import *
from game_files.config import *


def game_setup():
    nome = input("Player name: ")
    plr = Player(name=nome, health=100.0, attack=5, defense=2)
    return plr


plr = game_setup()
game_manager = GameManager(plr)
clear_screen()

game_manager.start()

print("\n")
input("Press any key to exit...")
