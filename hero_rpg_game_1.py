from character_rpg_game_1 import Character

class Hero(Character):

    def print_status(self):
            print("You have %d health and %d power." % (self.health, self.power))
            
    def attack(self, target):
        target.health -= self.power
        print("You do %d damage to the goblin." % self.power)



    







