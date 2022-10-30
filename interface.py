import os



class Interface():
    def clear():
        clear = lambda: os.system('cls')
        clear()


    def pressEnter():
        input("\n\nPress Enter to continue...")
        Interface.clear()


    def titleCard():
        Interface.clear()
        print("--------------[ Turn-Based Combat ]--------------")
        Interface.pressEnter()


    def characterInfo(pc):
        print(f"\n[{pc.name}]\n\nHp: {pc.hp} / {pc.max_hp}\nLevel: {pc.level} | Xp: {pc.xp}\nInitiative: {pc.init} | Dodge Class: {pc.dodge_class}\n")

        if pc.equipped['mainHand'] is not None:
            mainHand = pc.equipped['mainHand'].name
        else:
            mainHand = "None"
        if pc.equipped['offHand'] is not None:
            offHand = pc.equipped['offhand']
        else:
            offHand = "None"
        print(f"Main-Hand: {mainHand} | Off-Hand: {offHand}")

        if pc.equipped['wearable']:
            print(f"Wearing:")
            for item in list(pc.equipped['wearable']):
                print(f"- {item['name']}")
        else:
            print(f"Wearing: {pc.equipped['wearable']}")
        if pc.inventory:
            print(f"Inventory:")
            for item in list(pc.inventory):
                print(f"- {item['inventory']}")
        else:
            print("Inventory: None")


    def mainMenu(pc):
        print("\n\t--- [Main Menu] ---")
        Interface.characterInfo(pc)
        userInput = input("\n\n1 - Next Encounter\n2 - Heal\n3 - Quit Game\n\n\n")
        return userInput

    
    def encounterStart():
        Interface.clear()
        print(f"\n\t--- [Encounter Starting] ---")
        Interface.pressEnter()


    def encounterEnd(encounter):
        print(f"\n\t--- [Encounter Ended] ---\n")

        if encounter.pc not in encounter.combatants:
            print(f"{encounter.pc.name} has fallen in battle!")
        else:
            print(f"{encounter.pc.name} gained {encounter.player_xp} xp.")

        if encounter.all_downed:
            print(f"\nCasualties:")
            for lifeform in encounter.all_downed:
                print(f"- {lifeform.name}")
        
        Interface.pressEnter()

    
    def levelupMessage(lifeform):
        Interface.clear()
        print(f"\t--- [Levelup] ---")
        print(f"\n{lifeform.name} has reached experience level {lifeform.level}!")
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
        