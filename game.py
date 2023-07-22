from game_files.entities import *
from game_files.encounter import *

#nome, vida, dano, chance de critico
lucas = Player('lucas', 100.0, 1, 0.05, 1.5)
slime = Enemy('Slime', 10.0, 1)



next_encounter = Encounter(lucas,slime)
next_encounter.start()

