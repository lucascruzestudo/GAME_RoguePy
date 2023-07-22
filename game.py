from game_files.entities import *
from game_files.encounter import *
from colorama import Fore, Style, init as colorama_init
import random
from time import sleep

colorama_init()

def game_setup():
    nome = input("Warrior name: ")
    plr = Player(nome)
    return plr

plr = game_setup()
os.system('clear||cls')

# inimigos

#nome, vida, dano, nivel
enemies_list = [
    Enemy('Slime', 10.0, 1, 1),
    Enemy('Ogre', 50.0, 1, 2),
]


while plr.is_alive() and enemies_list:
    
    selected_enemy = random.choice(enemies_list)
    
    enemies_list.remove(selected_enemy)
    
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
