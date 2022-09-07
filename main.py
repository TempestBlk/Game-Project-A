# A Turn-based Combat Module
#
# TODO:
#   combo class based on multi-weapon atks and more!
#   entity "base"/"max" stats to reset obj attribute
#   buff/debuff classes for timed/lingering effects in/out of combat

from entities import PlayerCharacter
from encounters import random_encounter
from menu import Menu
from debug import *

def shutdown():
    print("\n\n\n\n--------------[ Shutting Down ]--------------\n\n\n\n")

def main():
    print("\n\n\n\n--------------[ Turn-Based Combat Module ]--------------")
    pc = PlayerCharacter()
    menu = Menu()
    
    keep_running = True # main game loop
    while keep_running:
        choice = menu.display_menu("Main Menu", ["random encounter", "recover", "debug", "quit"]) 
        if choice == "1":
            random_encounter(pc)
        elif choice == "2":
            pc.set_hp(pc.get_max_hp())
            pc.rm_status('downed')
        elif choice == "3":
            debug(pc) # runs test code in debug.py
        elif choice in ["4", "q"]: # TODO: add letters to valid input
            keep_running = False
            shutdown()
    

if __name__ == '__main__':
    main()