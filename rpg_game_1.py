from hero_rpg_game_1 import Hero
from goblin_rpg_game_1 import Goblin

daHero = Hero(10, 5)
daGoblin = Goblin(6, 2)

while daGoblin.alive() and daHero.alive():
    print("What do you want to do?: ")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    user_input = input(": ")
    if user_input == "1":
        daHero.attack(daGoblin)
        daGoblin.print_status()
        daGoblin.attack(daHero)
        daHero.print_status()
        if not daGoblin.alive():
            print("The goblin is dead.")
    elif user_input == "2":
        daGoblin.attack(daHero)
        daHero.print_status()
    elif user_input == "3":
        print("Goodbye.")
    else:
        print("Invalid input %r" % user_input)


   
    

    
    
        


