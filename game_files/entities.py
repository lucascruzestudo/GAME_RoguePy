from random import random, uniform
from colorama import Fore, Style


class Entity:
    def __init__(self, name, health, attack, defense):
        self._name = name.upper()
        self._health = health
        self._attack = attack
        self._defense = defense
        self._maxhealth = health

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
    def maxhealth(self):
        return self._maxhealth

    @maxhealth.setter
    def maxhealth(self, new_value):
        self._maxhealth = new_value

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
        attack = attack**2 / (attack + self.defense)
        attack = round(attack * 4) / 4
        damage = f"{Fore.RED}{Style.BRIGHT}{attack}{Style.RESET_ALL}"
        print(f"{self.name} took {damage} damage.\n")
        self.health -= attack

    def show_status(self):
        return (
            f"{self.name} HP: {Fore.RED}{self.health}/{self.maxhealth}{Style.RESET_ALL}"
        )


class Player(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self._crit_odd = 0.05
        self._crit_amp = 1.25
        self._potions = 3
        self._current_floor = 1
        self._defeated_enemies = 0
        self._gold = 0

    def odd_handler(self, chance):
        floor = random()
        return floor <= chance

    @staticmethod
    def _critical_hit_message():
        return Fore.RED + Style.BRIGHT + "CRITICAL HIT!" + Style.RESET_ALL

    def deal_damage(self, target):

        print(f"{self.name} attacks {target.name}!")

        damage_range = uniform(0.8, 1.2)
        mod_attack = self.attack * damage_range

        if self.odd_handler(self.crit_odd):
            print(self._critical_hit_message())
            target.receive_damage(mod_attack * self.crit_amp)
        else:
            target.receive_damage(mod_attack)

    def use_potion(self):

        print(f"{self.name} uses a potion to heal {Fore.RED}20 HP{Style.RESET_ALL}.\n")

        self.potions -= 1

        if (self.health + 20) > self.maxhealth:
            self.health = self.maxhealth

        else:
            self.health += 20

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
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, new_value):
        self._gold = new_value

    @property
    def potions(self):
        return self._potions

    @potions.setter
    def potions(self, new_value):
        self._potions = new_value

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, new_value):
        self._current_floor = new_value

    @property
    def defeated_enemies(self):
        return self._defeated_enemies

    @defeated_enemies.setter
    def defeated_enemies(self, new_value):
        self._defeated_enemies = new_value

    @property
    def crit_amp(self):
        return self._crit_amp

    @crit_amp.setter
    def crit_amp(self, new_value):
        self._crit_amp = new_value


class Enemy(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
