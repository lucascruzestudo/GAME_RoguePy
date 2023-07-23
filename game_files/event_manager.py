from game_files.encounter import Encounter
from game_files.shop import Shop

class EventManager:
    
    def __init__(self, player):
        self.player = player

    def handle_encounter(self, enemy):
        encounter = Encounter(self.player, enemy)
        encounter.start()
        del encounter
        
    def visit_shop(self):
        shop = Shop(self.player)