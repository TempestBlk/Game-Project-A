from debug import Debug
from encounters import Encounter
from inventory import Inventory
from lifeforms import PlayerCharacter
from interface import Interface
from items import Weapon, Wearable
from npcs import QuartermasterMathias, SeniorResearcherLydia



def main():
    gameRunning = True
    while gameRunning:

        userInput = Interface.mainMenu(pc)
        
        
        if userInput == "1":
            Interface.encounterMenu(pc, Encounter)
        
        elif userInput == "2":
            Inventory.open(pc)
        
        elif userInput == "3":
            QuartermasterMathias.startDialogue(pc)

        elif userInput == "4":
            SeniorResearcherLydia.startDialogue(pc)

        elif userInput == "5":
            gameRunning = False

        elif userInput == "p":
            Debug.show_protection(pc)

        Interface.clear()


if __name__ == "__main__":
    Interface.startup()

    pc = PlayerCharacter("Jr Researcher Krycek", "researcher") # NOTE: "if save file, load pc from file, else start newgame"
    starting_items = [Weapon(Weapon.metal_pipe), Weapon(Weapon.shiv), Wearable(Wearable.junior_researcher_coat), Wearable(Wearable.tf5_fireteam_vest), Weapon(Weapon.f_collective_solspear)]
    pc.inventory += starting_items
    pc.equip_wearable(Wearable(Wearable.torn_clothes))

    main()
    Interface.shutdown()