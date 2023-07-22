from colorama import Fore, Style
from time import sleep
import os

PAUSE_DURATION = 3

class Encounter:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.round_counter = 0
        self._fled = False
        self.PAUSETIME = 2
        
    @property
    def fled(self):
        return self._fled
    
    @fled.setter
    def fled(self, value):
        self._fled = value

    def print_status(self):
        
        print(f"{self.player.name} HP: {Fore.RED}{self.player.health}{Style.RESET_ALL}")
        print(f"{self.enemy.name} HP: {Fore.RED}{self.enemy.health}{Style.RESET_ALL}\n")

    def player_turn(self):
        
        print("Choose your action:")
        print(Style.BRIGHT)
        print(f"1. Attack")
        print(f"2. Flee")
        print(Style.RESET_ALL)

        while True:
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.player.attack(self.enemy)
    
                break
            elif choice == "2":
                self.fled = True
                break
            else:
                print("Invalid choice. Try again.")

    def enemy_turn(self):
        
        self.enemy.attack(self.player)
            


    def start(self):
        
        print(f"{Fore.YELLOW}{Style.BRIGHT}{self.enemy.name}{Style.RESET_ALL} engages!\n")

        while self.player.is_alive() and self.enemy.is_alive() and self.fled == False:
            
            self.round_counter += 1

            print(f"--- Round {self.round_counter} ---")
            self.print_status()
            
            self.player_turn()

            if self.enemy.is_alive() and not self.fled:
                self.enemy_turn()
            
        self.end()

    def end(self):
        
        if self.fled == True:
            print(f"{self.player.name} fled the battle.")
        elif self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
        else:
            print(f"{self.enemy.name} has defeated {self.player.name}!")
            