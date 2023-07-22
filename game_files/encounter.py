class Encounter:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        print("An encounter has started!")
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack(self.player)
        self.end()

    def end(self):
        if self.player.is_alive():
            print(f"{self.player.name} has defeated {self.enemy.name}!")
        else:
            print(f"{self.enemy.name} has defeated {self.player.name}!")