from debug import Debug
from lifeforms import PlayerCharacter
from encounters import Encounter
from interface import Interface
from items import Weapons, Weapon



def main():
    gameRunning = True
    while gameRunning:
        userInput = Interface.mainMenu(pc) 
        if userInput == "1":
            if pc.hp > 0:
                Interface.clear()
                Encounter(pc, difficulty=1)
            else:
                print(f"\n{pc.name} is dead...")
                Interface.pressEnter()
        elif userInput == "2":
            pc.hp = pc.max_hp
            Interface.clear()
        elif userInput == "3":
            print("\n--------------[ Shutting Down ]--------------")
            Interface.pressEnter()
            gameRunning = False
        elif userInput == "test":
            Interface.clear()
            Debug.test_npcid()

    print("\n\n")


if __name__ == "__main__":
    Interface.titleCard()

    pc = PlayerCharacter("Jr Researcher Krycek", "researcher") # NOTE: "if save file, load pc from file, else start newgame"
    pc.equip_weapon(Weapon(Weapons.metal_pipe))

    main()