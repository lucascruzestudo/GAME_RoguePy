from random import random

class Entity:
    
    def __init__(self, name, health, damage, level):
        self._name = name.upper()
        self._health = health
        self._damage = damage
        self._level = level
        
    @property
    def name(self):
        return self._name
    
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
        print(f"{self.name} took {amount} damage.\n")
        self.health -= amount
    
class Player(Entity):
    def __init__(self, name, health=100.0, damage=1, level=1):
        super().__init__(name, health, damage, level)
        self._crit_odd = 0.05
        self._crit_amp = 1.25
        
    def attack(self, target):
            print(f"{self.name} attacks {target.name}!")
            crit_floor = random()
            if crit_floor <= self.crit_odd:
                print("Critical hit!".upper())
                target.receive_damage(self.damage * self.crit_amp)
            else:
                target.receive_damage(self.damage)
                
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
