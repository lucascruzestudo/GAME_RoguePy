from game_files.encounter import Encounter
from game_files.shop import Shop
from game_files.enemy_table import floors
from game_files.entities import Enemy
from game_files.config import *
from colorama import Fore, Style, init as colorama_init
from time import sleep
from os import system

colorama_init()
import random


class GameManager:
    def __init__(self, player):
        self.player = player
        self.event_manager = EventManager(self.player)

    def start(self):
        while self.player.is_alive():
            while self.player.current_floor <= 2 and self.player.is_alive():
                enemy_pool = floors.get(self.player.current_floor)
                while (
                    self.player.defeated_enemies < MONSTERS_PER_FLOOR
                    and self.player.is_alive()
                ):
                    self.show_player_status()
                    selected_enemy_params = random.choice(enemy_pool)
                    selected_enemy = Enemy(**selected_enemy_params)
                    self.event_manager.handle_encounter(selected_enemy)
                    self.event_manager.random_event()
                self.next_floor()
            if self.player.current_floor > 2:
                break
        self.end()
        
    def show_player_status(self):
        system("cls||clear")
        print(f"{self.player.name} {Fore.RED}{Style.BRIGHT}{self.player.health}/{self.player.maxhealth} HP{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}{self.player.gold} GOLD {Fore.GREEN}{self.player.attack} ATK {Fore.CYAN}{self.player.defense} DEF {Style.RESET_ALL}\n")
        print(f"\nFLOOR {self.player.current_floor} - {MONSTERS_PER_FLOOR - self.player.defeated_enemies} monsters remaining.")
        input("Press enter to continue your adventure...")

    def next_floor(self):
        system("cls||clear")
        print(f"{self.player.name} advances...")
        self.player.defeated_enemies = 0
        self.player.current_floor += 1
        sleep(PAUSE_DURATION)

    def end(self):
        system("cls||clear")
        if self.player.is_alive():
            print(f"{self.player.name} ESCAPED THE DUNGEON!")
        else:
            print(f"{self.player.name} died inside the dungeon.")
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
        sleep(PAUSE_DURATION)


class EventManager:
    def __init__(self, player):
        self.player = player

    def handle_encounter(self, enemy):
        encounter = Encounter(self.player, enemy)
        encounter.start()
        del encounter
        
    def random_event(self):
        system("cls||clear")
        random.choice([self.find_chest(),]) # inserir mais eventos
        sleep(PAUSE_DURATION)

    def visit_shop(self):
        shop = Shop(self.player)
    
    def find_chest(self):
        result = random.choice(['gold', 'potion', 'empty'])
        if result == 'gold':
            gold = random.randint(10,20) # tenebroso
            print(f"{self.player.name} finds a chest containing {gold} gold!")
            self.player.gold += gold
        if result == 'potion':
            potions = random.randint(1,3)
            print(f"{self.player.name} finds a chest containing {potions} potion(s)!")
            self.player.potions += potions
        if result == 'empty':
            print(f"{self.player.name} found a chest but it was empty!")
            
        
