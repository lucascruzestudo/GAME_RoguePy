from colorama import Fore, Style
from time import sleep
import os

PAUSE_DURATION = 3

class Encounter:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.round_counter = 0
        self.PAUSETIME = 2
        self._player_action = None
        
    @property
    def player_action(self):
        return self._player_action
    
    @player_action.setter
    def player_action(self, value):
        self._player_action = value
        
    def pre_turn(self):
        print("Choose your action:")
        print(Style.BRIGHT)
        print(f"1. Attack")
        print(f"2. Flee")
        print(Style.RESET_ALL)

        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                self.player_action = "attack"
                break
            elif choice == "2":
                self.player_action = "flee"
                break
            else:
                print("Invalid choice. Try again.")
                
    def execute_turn(self):
        
        os.system('clear||cls')
        
        if self.player_action == "attack":
            self.player.attack(self.enemy)
            
        self.enemy.attack(self.player)
        
        sleep(PAUSE_DURATION)

    def battle_status(self):
        
        print(f"{self.player.name} HP: {Fore.RED}{self.player.health}{Style.RESET_ALL}")
        print(f"{self.enemy.name} HP: {Fore.RED}{self.enemy.health}{Style.RESET_ALL}\n")
            
    def start(self):
        
        os.system('clear||cls')

        print(f"{self.enemy.name} engages!\n")
        
        sleep(PAUSE_DURATION)


        while self.player.is_alive() and self.enemy.is_alive():
            
            os.system('clear||cls')
            
            self.round_counter += 1

            print(f"--- Round {self.round_counter} ---")
            self.battle_status()

            self.pre_turn()

            if self.player_action == "flee":
                break

            self.execute_turn()
            
            self.player_action = None

        self.end()

    def end(self):
        
        os.system('clear||cls')
        
        if self.player_action == "flee":
            print(f"{self.player.name} fled the battle.")
        elif self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
        else:
            print(f"{self.enemy.name} has defeated {self.player.name}!")
            
        sleep(PAUSE_DURATION)

            
        os.system('clear||cls')
            