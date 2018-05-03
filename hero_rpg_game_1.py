#blueprint for the object to be given to a variable in your other file
class Hero(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def print_status(self):
            print("You have %d health and %d power." % (self.health, self.power))

    def alive(self):
        return self.health >0
            
            
    def attack(self, target):
        target.health -= self.power
        print("You do %d damage to the goblin." % self.power)



    







