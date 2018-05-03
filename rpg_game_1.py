from hero_rpg_game_1 import *
from goblin_rpg_game_1 import *

daHero = Hero(10, 5)

daGoblin = Goblin(6, 2)



while daGoblin.alive and daHero.alive:
    daHero.print_status
    daHero.attack(daGoblin)
    daGoblin.attack(daHero)
    daGoblin.print_status

    
    
        


