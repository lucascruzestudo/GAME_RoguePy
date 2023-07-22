from random import random
from colorama import Fore, Style

class Entity:
    
    def __init__(self, name, health, damage, level):
        self._name = name.upper()
        self._health = health
        self._damage = damage
        self._level = level
        
    @property
    def name(self):
        return Fore.YELLOW + Style.BRIGHT + self._name + Style.RESET_ALL
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_value):
        self._health = new_value
    
    @property
    def damage(self):
        return self._damage
    
    @property
    def level(self):
        return self._level
    
    def is_alive(self):
        return self.health > 0
    
    def attack(self, target):
            print(f"{self.name} attacks {target.name}!")
            target.receive_damage(self.damage)

    def receive_damage(self, amount):
        formatted_damage = f"{Fore.RED}{Style.BRIGHT}{amount}{Style.RESET_ALL}"
        print(f"{self.name} took {formatted_damage} damage.\n")
        self.health -= amount
    
class Player(Entity):
    def __init__(self, name, health=100.0, damage=1, level=1):
        super().__init__(name, health, damage, level)
        self._crit_odd = 1
        self._crit_amp = 1.25
        
    @staticmethod
    def _critical_hit_message():
        return Fore.RED + Style.BRIGHT + "CRITICAL HIT!" + Style.RESET_ALL
        
    def attack(self, target):
        
            print(f"{self.name} attacks {target.name}!")
            crit_floor = random()
            if crit_floor <= self.crit_odd:
                print(self._critical_hit_message())
                target.receive_damage(self.damage * self.crit_amp)
            else:
                target.receive_damage(self.damage)
                
    @property
    def name(self):
        return Fore.BLUE + Style.BRIGHT + self._name + Style.RESET_ALL
                
    @property
    def crit_odd(self):
        return self._crit_odd
    
    @crit_odd.setter
    def crit_odd(self, new_value):
        self._crit_odd = new_value
        
    @property
    def crit_amp(self):
        return self._crit_amp
    
    @crit_amp.setter
    def crit_amp(self, new_value):
        self._crit_amp = new_value

class Enemy(Entity):
    def __init__(self, name, health, damage, level):
        super().__init__(name, health, damage, level)
