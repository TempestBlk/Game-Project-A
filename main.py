from debug import Debug
from encounters import Encounter
from lifeforms import PlayerCharacter
from interface import Interface
from items import Weapon, Weapons, Wearable, Wearables



def main():
    gameRunning = True
    while gameRunning:

        userInput = Interface.mainMenu(pc)
        
        
        if userInput == "1":
            Interface.encounterMenu(pc, Encounter)
        
        elif userInput == "2":
            Interface.inventoryMenu(pc)
        
        elif userInput == "3":
            Interface.merchantMenu(pc)

        elif userInput == "4":
            Interface.doctorMenu(pc)

        elif userInput == "5":
            gameRunning = False

        elif userInput == "p":
            Debug.show_protection(pc)

        Interface.clear()


if __name__ == "__main__":
    Interface.startup()

    pc = PlayerCharacter("Jr Researcher Krycek", "researcher") # NOTE: "if save file, load pc from file, else start newgame"
    starting_items = [Weapon(Weapons.metal_pipe), Weapon(Weapons.shiv), Wearable(Wearables.junior_researcher_coat)]
    pc.inventory += starting_items

    main()
    Interface.shutdown()