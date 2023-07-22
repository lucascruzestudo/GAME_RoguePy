from game_files.entities import *
from game_files.encounter import *
import random
from time import sleep


nome = input("Informe o nome do guerreiro: ")
plr = Player(nome)
print("Prepare-se para a maior batalha de sua vida...")
sleep(1)

# inimigos

#nome, vida, dano, nivel
enemies_list = [
    Enemy('Slime', 10.0, 1, 1),
    Enemy('Ogre', 5.0, 1, 2),
]


while plr.is_alive() and enemies_list:
    
    selected_enemy = random.choice(enemies_list)
    
    enemies_list.remove(selected_enemy)
    
    encounter = Encounter(plr, selected_enemy)
    encounter.start()
    del encounter

if plr.is_alive():
    print(f"{plr.name} SURVIVED THE HORDE!")
else:
    print(f"{plr.name} DIED!")
