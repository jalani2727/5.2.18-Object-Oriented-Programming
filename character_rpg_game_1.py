class Character(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        return self.health >0

    def print_status(self, either):
        if either.power == 2:
            print("The goblin has %d health and %d power." % (self.health, self.power))
        if either.power == 5:
            print("You have %d health and %d power." % (self.health, self.power))
            