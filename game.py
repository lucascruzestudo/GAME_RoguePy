from game_files.entities import *
from game_files.encounter import *
from game_files.enemy_table import enemies
from colorama import Fore, Style, init as colorama_init
import random
from time import sleep

colorama_init()

def game_setup():
    nome = input("Warrior name: ")
    plr = Player(name=nome, health=100.0, attack=10, defense=2)
    return plr

plr = game_setup()
os.system('clear||cls')

while plr.is_alive() and enemies:
    
    selected_enemy = random.choice(enemies)
    
    enemies.remove(selected_enemy)
    
    encounter = Encounter(plr, selected_enemy)
    encounter.start()
    del encounter

if plr.is_alive():
    print(f"{plr.name} ESCAPED THE DUNGEON!")
    
else:
    print(f"{plr.name} died inside the dungeon.")
    
    img = """
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\\\\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_|
    """
    print(f"{Fore.RED}{Style.BRIGHT}{img}{Style.RESET_ALL}")

input()
