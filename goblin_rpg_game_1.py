from character_rpg_game_1 import Character

class Goblin(Character):
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

    def attack(self, target):
        if self.health > 0:
            # Goblin attacks hero
            target.health-= self.power
            print("The goblin does %d damage to you." % self.power)
            if target.health <= 0:
                print("You are dead.")