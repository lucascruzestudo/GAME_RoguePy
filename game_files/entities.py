from random import random, uniform

class Entity:
    def __init__(self, name, health, attack, defense):
        self.name = name.upper()
        self.health = health
        self.attack = attack
        self.defense = defense
        self.maxhealth = health
        self.miss_odd = 0.025

    def odd_handler(self, chance):
        floor = random()
        return floor <= chance

    def is_alive(self):
        return self.health > 0

    def deal_damage(self, target):
        print(f"{self.name} attacks {target.name}!")

        if self.odd_handler(self.miss_odd):
            print(f"{self.name} misses!\n")
        else:
            damage_range = uniform(0.8, 1.2)
            mod_attack = self.attack * damage_range
            target.receive_damage(mod_attack)

    def receive_damage(self, attack):
        attack = attack ** 2 / (attack + self.defense)
        attack = round(attack * 4) / 4
        print(f"{self.name} took {attack} damage.\n")
        self.health -= attack

    def show_status(self):
        return f"{self.name} HP: {self.health}/{self.maxhealth}"


class Player(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.crit_odd = 0.05
        self.crit_amp = 1.25
        self.potions = 3
        self.current_floor = 1
        self.defeated_enemies = 0
        self.gold = 0

    @staticmethod
    def _critical_hit_message():
        return "CRITICAL HIT!"

    def deal_damage(self, target):
        print(f"{self.name} attacks {target.name}!")

        if self.odd_handler(self.miss_odd):
            print(f"{self.name} misses!\n")
        else:
            damage_range = uniform(0.8, 1.2)
            mod_attack = self.attack * damage_range

            if self.odd_handler(self.crit_odd):
                print(self._critical_hit_message())
                target.receive_damage(mod_attack * self.crit_amp)
            else:
                target.receive_damage(mod_attack)

    def use_potion(self):
        if self.potions <= 0:
            print(f"{self.name} has no potions left!")

        heal_amount = self.maxhealth * 0.2
        if (self.health + heal_amount) > self.maxhealth:
            self.health = self.maxhealth
        else:
            self.health += heal_amount

        print(f"{self.name} uses a potion to heal {heal_amount}.\n")
        self.potions -= 1


class Enemy(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
