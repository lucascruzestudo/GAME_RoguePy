from game_files.entities import *
from game_files.encounter import *

#nome
lucas = Player('lucas')

#nome, vida, dano, nivel
slime = Enemy('Slime', 10.0, 1, 1)



next_encounter = Encounter(lucas,slime)
next_encounter.start()

