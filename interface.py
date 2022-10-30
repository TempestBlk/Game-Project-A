import os
from items import Weapons, Weapon



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
            print(f"\n[{pc.name}]\n\nHp: {pc.hp} / {pc.max_hp}\nLevel: {pc.level} | Xp: {pc.xp}\nInitiative: {pc.init} | Dodge Class: {pc.dodge_class}\nGold Flakes: {pc.gold_flakes}\n")

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
            print(f"\nWearing:")
            for item in list(pc.equipped['wearable']):
                print(f"- {item['name']}")
        else:
            print(f"\nWearing: None")


    def mainMenu(pc):
        print("\n\t--- [Main Menu] ---")
        Interface.characterInfo(pc)
        userInput = input("\n\n[1] Next Encounter\n[2] Inventory\n[3] Merchant\n[4] Doctor\n[5] Quit Game\n\n\n")
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


    def encounterMenu(pc, Encounter):
        if pc.hp > 0:
            Interface.clear()
            userInput = input("\nChoose a difficulty.\n[1] Easy\n[2] Medium\n\n\n")
            if userInput == "1":
                Encounter(pc, difficulty=1)
            elif userInput == "2":
                Encounter(pc, difficulty=2)
        else:
            print(f"\n{pc.name} is dead...")
            Interface.pressEnter()


    def merchantMenu(pc):
        showMerchant = True
        while showMerchant:
            Interface.clear()
            print("\n\t--- [Merchant] ---")
            print("\n[Quartermaster Mathias]\n")
            print("\nWelcome. How can I help?\n")
            userInput = input("\n[1] Weapons\n[2] Wearables\n\n\n")
            if userInput == "1":
                Interface.clear()
                print("\n\t--- [Merchant] ---")
                print("\n[Quartermaster Mathias]\n")
                print("\nTired of beating Mindless with your fists?\nHave a look at these.\n")
                userInput = input(f"\n[1] Shiv ({Weapons.shiv['basePrice'] * 0})\n[2] Metal Pipe ({Weapons.metal_pipe['basePrice'] * 0})\n\n\n")
                if userInput == "1":
                    pc.equip_weapon(Weapon(Weapons.shiv))
                elif userInput == "2":
                    pc.equip_weapon(Weapon(Weapons.metal_pipe))
            elif userInput == "2":
                print("\n\nSorry, I'm all out of body armor...")
                Interface.pressEnter()
            else:
                showMerchant = False


    def doctorMenu(pc):
        Interface.clear()
        print("\n\t--- [Doctor] ---")
        print("\n[Sr Researcher Lydia]\n")
        if pc.hp == pc.max_hp:
            print("\nYou're healthy enough. Stop wasting my time!")
        elif pc.hp > pc.max_hp * 0.5:
            print("\nNot too bad, let me patch you up.")
        elif pc.hp > pc.max_hp * 0.25:
            print("\nYou're not looking too hot...\nHave a seat and bite down on this.")
        elif pc.hp > 0:
            print("\nSet them down here! We'll start surgery immediately.")
        else:
            print(f"\n{pc.name} is dead...\nGet their body in the Anubis Chamber.")
        pc.hp = pc.max_hp
        Interface.pressEnter()


    def inventoryMenu(pc):
        inInventory = True
        while inInventory:
            Interface.clear()
            Interface.characterInfo(pc, stats=False)
            if pc.inventory:
                print(f"\nInventory:")
                item_num = 0
                item_dict = {}
                for item in list(pc.inventory):
                    item_num += 1
                    item_dict[f"{item_num}"] = item
                    print(f"[{item_num}] {item.name}")
                userInput = input("\n")
                if userInput in item_dict:
                    selected_item = item_dict[userInput]
                    if type(selected_item) is Weapon:
                        userInput = input("\n[1] Equip\n[2] Drop\n\n")
                        if userInput == "1":
                            pc.equip_weapon(selected_item)
                        elif userInput == "2":
                            pc.inventory.remove(selected_item)
                else:
                    inInventory = False

            else:
                print("\nInventory: None")
                inInventory = False
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
        