#blueprint for the object to be given to a variable in your other file
class Hero(object):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        while self.alive():
            print("You have %d health and %d power." % (self.health, self.power))
            
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

    def attack(self, target):
        self.print_status
        print("What do you want to do?: ")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        user_input = input(" : ")
        if user_input == "1":
            # Hero attacks goblin
            target.health -= self.power
            print("You do %d damage to the goblin." % self.power)
            if target.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
        else:
            print("Invalid input %r" % user_input)



    







