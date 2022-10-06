# A Turn-based Combat Module
#
# TODO:
#   combo class based on multi-weapon atks and more!
#   entity "base"/"max" stats to reset obj attribute
#   buff/debuff classes for timed/lingering effects in/out of combat

from entities import PlayerCharacter
from encounters import Encounter
from menu import Menu
from debug import Debug

def shutdown():
    print("\n\n\n\n[Main] Shutting down...\n\n\n\n")

def main():
    print("\n\n\n\n[Main] Starting Turn-Based Combat Module")
    pc = PlayerCharacter()
    
    keep_running = True # main game loop
    while keep_running:
        choice = Menu.option_menu("Main Menu", ["random encounter", "character stats", "heal character", "quit"]) 
        if choice == 1:
            if pc.hp > 0:
                encounter = Encounter(pc)
                encounter.run_encounter()
            else:
                print("You're already dead! Restore first.")
        elif choice == 2:
            Debug.check_pc(pc)
        elif choice == 3:
            pc.set("hp", pc.get("max_hp"))
            pc.rm_status('downed') # NOTE: currently only removes the 'downed' status
        elif choice == 4:
            keep_running = False
            shutdown()
    

if __name__ == '__main__':
    main()