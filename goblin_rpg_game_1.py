class Goblin(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        return self.health >0
            
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

    def attack(self, target):
        if self.health > 0:
            self.print_status()
            # Goblin attacks hero
            target.health-= self.power
            print("The goblin does %d damage to you." % self.power)
            if target.health <= 0:
                print("You are dead.")