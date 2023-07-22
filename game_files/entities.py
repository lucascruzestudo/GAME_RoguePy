from random import random, uniform
from colorama import Fore, Style

class Entity:
    
    def __init__(self, name, health, attack, defense):
        self._name = name.upper()
        self._health = health
        self._attack = attack
        self._defense = defense
        
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
    def attack(self):
        return self._attack
    
    @property
    def defense(self):
        return self._defense
    
    def is_alive(self):
        return self.health > 0
    
    def deal_damage(self, target):
        print(f"{self.name} attacks {target.name}!")
        damage_range = uniform(0.8, 1.2)
        mod_attack = self.attack * damage_range
        target.receive_damage(mod_attack)

    def receive_damage(self, attack):
        attack = attack ** 2 / (attack + self.defense)
        attack = round(attack * 4) / 4 
        damage = f"{Fore.RED}{Style.BRIGHT}{attack}{Style.RESET_ALL}"
        print(f"{self.name} took {damage} damage.\n")
        self.health -= attack
    
class Player(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self._crit_odd = 0.05
        self._crit_amp = 1.25
        
    @staticmethod
    def _critical_hit_message():
        return Fore.RED + Style.BRIGHT + "CRITICAL HIT!" + Style.RESET_ALL
        
    def deal_damage(self, target):
        
            print(f"{self.name} attacks {target.name}!")
            
            damage_range = uniform(0.8, 1.2)
            mod_attack = self.attack * damage_range
            
            crit_floor = random()
            if crit_floor <= self.crit_odd:
                print(self._critical_hit_message())
                target.receive_damage(mod_attack * self.crit_amp)
            else:
                target.receive_damage(mod_attack)
                
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
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
