from time import sleep
import os
from game_files.config import *


class Encounter:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn_counter = 0
        self._player_action = None

    @property
    def player_action(self):
        return self._player_action

    @player_action.setter
    def player_action(self, value):
        self._player_action = value

    def pre_turn(self):
        print("Choose your action:")
        print(f"\n1. Attack")
        print(f"2. Potion ({self.player.potions})")
        print(f"3. Flee\n")

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.player_action = "attack"
                break
            elif choice == "2":
                self.player_action = "potion"
                break
            elif choice == "3":
                self.player_action = "flee"
                break
            else:
                print("Invalid choice. Try again.\n")

    def execute_turn(self):

        os.system("cls||clear")

        if self.player_action == "attack":
            if self.player.health > 0:
                self.player.deal_damage(self.enemy)

        elif self.player_action == "potion":
            if self.player.health > 0 and (self.player.health < self.player.maxhealth):
                self.player.use_potion()
            else:
                print(f"{self.player.name} health is already at max.\n")

        elif self.player_action == "fail_flee":
            print(f"{self.player.name} failed fleeing!\n")

        if self.enemy.health > 0:
            self.enemy.deal_damage(self.player)

        sleep(PAUSE_DURATION)

    def battle_status(self):

        print(self.player.show_status())
        print(self.enemy.show_status())

    def start(self):

        os.system("cls||clear")

        print(f"a {self.enemy.name} engages!\n")

        sleep(PAUSE_DURATION)

        while self.player.is_alive() and self.enemy.is_alive():

            os.system("cls||clear")

            self.turn_counter += 1

            print(f"--- Turn {self.turn_counter} ---")
            self.battle_status()

            self.pre_turn()

            if self.player_action == "flee":
                if self.player.odd_handler(0.40):
                    break
                else:
                    self.player_action = "fail_flee"

            self.execute_turn()

            self.player_action = None

        self.end()

    def end(self):

        os.system("cls||clear")

        if self.player_action == "flee":
            print(f"{self.player.name} fled the battle.")
        elif self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
            self.player.defeated_enemies += 1
        else:
            print(f"{self.enemy.name} has defeated {self.player.name}!")

        sleep(PAUSE_DURATION)

        os.system("cls||clear")
