from game_files.encounter import Encounter
from game_files.shop import Shop
from game_files.enemy_table import floors
from game_files.entities import Enemy
from game_files.config import *
import random
from time import sleep
from os import system

class GameManager:
    def __init__(self, player):
        self.player = player

    def start(self):
        while self.player.is_alive() and self.player.current_floor <= 2:
            enemy_pool = floors.get(self.player.current_floor)

            while (
                self.player.defeated_enemies < MONSTERS_PER_FLOOR
                and self.player.is_alive()
            ):
                self.player.show_player_status()
                selected_enemy_params = random.choice(enemy_pool)
                selected_enemy = Enemy(**selected_enemy_params)
                self.handle_encounter(selected_enemy)
                self.random_event()

            self.next_floor()

        self.end()

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
            print(img)
        sleep(PAUSE_DURATION)

    def handle_encounter(self, enemy):
        encounter = Encounter(self.player, enemy)
        encounter.start()
        del encounter

    def random_event(self):
        system("cls||clear")
        random.choice([self.find_chest(),]) # insert more events
        sleep(PAUSE_DURATION)
        
    def visit_shop(self):
        shop = Shop(self.player)

    def find_chest(self):
        result = random.choice(["gold", "potion", "empty"])

        if result == "gold":
            gold = random.randint(10, 20)
            print(f"{self.player.name} finds a chest containing {gold} gold!")
            self.player.gold += gold
        elif result == "potion":
            potions = random.randint(1, 3)
            print(f"{self.player.name} finds a chest containing {potions} potion(s)!")
            self.player.potions += potions
        else:
            print(f"{self.player.name} found a chest but it was empty!")
