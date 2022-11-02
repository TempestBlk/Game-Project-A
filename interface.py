import os
from items import Weapon, Weapon, Wearable



class Interface():
    def clear():
        clear = lambda: os.system('cls')
        clear()


    def pressEnter():
        input("\n\nPress Enter to continue... ")
        Interface.clear()


    def startup():
        Interface.clear()
        print("--------------[ Turn-Based Combat ]--------------")
        Interface.pressEnter()
    

    def shutdown():
        print("\n--------------[ Shutting Down ]--------------")
        Interface.pressEnter()


    def characterInfo(pc, stats=True):
        if stats:
            print(f"\n[{pc.name}]\n\nHp: {pc.hp}/{pc.max_hp} | Level: {pc.level} | Xp: {pc.xp}\nInitiative: {pc.init} | Dodge Class: {pc.dodge_class}\nGold Flakes: {pc.gold_flakes}\n")

        if pc.equipped['mainHand'] is not None:
            mainHand = f"{pc.equipped['mainHand'].name} ({pc.equipped['mainHand'].durability})"
        else:
            mainHand = "None"
        if pc.equipped['offHand'] is not None:
            offHand = f"{pc.equipped['offhand']} ({pc.equipped['mainHand'].durability})"
        else:
            offHand = "None"
        print(f"Main-Hand: {mainHand} | Off-Hand: {offHand}")

        if pc.equipped['wearable']:
            print(f"Wearing:")
            for item in list(pc.equipped['wearable']):
                print(f"- {item.name}  ({item.durability})")
        else:
            print(f"Wearing: None")


    def mainMenu(pc):
        print("\t--- [Main Menu] ---\n")
        Interface.characterInfo(pc)
        # print("\n")
        userInput = input("\n[1] Next Encounter\n[2] Inventory\n[3] Merchant\n[4] Doctor\n[5] Quit Game\n\n")
        return userInput

    
    def levelupMessage(lifeform):
        Interface.clear()
        print(f"\t--- [Levelup] ---")
        print(f"\n{lifeform.name} has reached experience level {lifeform.level}!")
        Interface.pressEnter()


    def encounterMenu(pc, Encounter):
        if pc.hp > 0:
            Interface.clear()
            userInput = input("\nChoose a difficulty.\n[1] Light\n[2] Average\n[3] Difficult\n\n[Enter] Go Back\n\n")
            if userInput == "1":
                Encounter(pc, difficulty=1)
            elif userInput == "2":
                Encounter(pc, difficulty=2)
            elif userInput == "3":
                Encounter(pc, difficulty=3)
        else:
            print(f"\n{pc.name} is dead...")
            Interface.pressEnter()
    

    def encounterStart():
        Interface.clear()
        print(f"\t--- [Encounter Starting] ---\n")
        Interface.pressEnter()


    def encounterEnd(encounter):
        print(f"\t--- [Encounter Ended] ---\n")

        if encounter.pc not in encounter.combatants:
            print(f"{encounter.pc.name} has fallen in battle!")
        else:
            print(f"{encounter.pc.name} gained {encounter.player_xp} xp.")

        if encounter.all_downed:
            print(f"\nCasualties:")
            for lifeform in encounter.all_downed:
                print(f"- {lifeform.name}")
        
        Interface.pressEnter()
    

    def error01():
        print("\n\n[ERROR-01] Encounter cant handle unaffiliated yet.")
        Interface.pressEnter()
    

    def error02():
        print("\n\n[ERROR-02] Include difficulty when building encounter.")
        Interface.pressEnter()


    def error03():
        print("\n\n[ERROR-03] Encounter difficulty level is invalid.")
        Interface.pressEnter()