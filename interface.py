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
        print("--------------[ Turn-Based Combat 2 ]--------------")
        Interface.pressEnter()
    
    def encounterStart():
        Interface.clear()
        print(f"\n\t--- [Encounter Starting] ---")
        Interface.pressEnter()

    def characterInfo(humanoid):
        print(f"\n[{humanoid.name}]\n\nHp: {humanoid.hp} / {humanoid.max_hp}\nLevel: 1 | Xp: {humanoid.xp}\nInitiative: {humanoid.init} | Dodge Class: {humanoid.dodge_class}\n")

        if humanoid.equipped['mainHand'] is not None:
            mainHand = humanoid.equipped['mainHand'].name
        else:
            mainHand = "None"
        if humanoid.equipped['offHand'] is not None:
            offHand = humanoid.equipped['offhand']
        else:
            offHand = "None"
        print(f"Main-Hand: {mainHand} | Off-Hand: {offHand}")

        if humanoid.equipped['wearable']:
            print(f"Wearing:")
            for item in list(humanoid.equipped['wearable']):
                print(f"- {item['name']}")
        else:
            print(f"Wearing: {humanoid.equipped['wearable']}")
        if humanoid.inventory:
            print(f"Inventory:")
            for item in list(humanoid.inventory):
                print(f"- {item['inventory']}")
        else:
            print("Inventory: None")

    def mainMenu(pc):
        print("\n\t--- [Main Menu] ---")
        Interface.characterInfo(pc)
        userInput = input("\n\n1 - Next Encounter\n2 - Heal\n3 - Quit Game\n\n\n")
        return userInput
    
    def error01():
        print("\n\n[ERROR-01] Encounter cant handle unaffiliated yet.")
        Interface.pressEnter()
    
    def error02():
        print("\n\n[ERROR-02] Include difficulty when building encounter.")
        Interface.pressEnter()

    def error03():
        print("\n\n[ERROR-03] Encounter difficulty level is invalid.")
        Interface.pressEnter()
        