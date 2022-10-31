import os
from items import Weapons, Weapon, Wearable



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
        userInput = input("\n\n[1] Next Encounter\n[2] Inventory\n[3] Merchant\n[4] Doctor\n[5] Quit Game\n\n\n")
        return userInput

    
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
        sell_mod = 0.25
        buy_mod = 1.20
        
        showMerchant = True
        while showMerchant:
            Interface.clear()
            print("\t--- [Merchant] ---\n")
            print("\n[Quartermaster Mathias]\n")
            print("Welcome. How can I help?\n")
            
            userInput = input("\n[1] Weapons\n[2] Wearables\n[3] Sell\n\n\n")
            
            if userInput == "1":
                Interface.clear()
                print("\t--- [Merchant] ---\n")
                print("\n[Quartermaster Mathias]\n")
                print("Tired of beating Mindless with your fists?\nHave a look at these.\n")
                
                userInput = input(f"\n[1] Shiv ({round(Weapons.shiv['basePrice'] * buy_mod)})\n[2] Metal Pipe ({round(Weapons.metal_pipe['basePrice'] * buy_mod)})\n[3] Bondprint Sabre ({round(Weapons.bondprint_sabre['basePrice'] * buy_mod)})\n\n\n")
        
                if userInput == "1":
                    if pc.gold_flakes >= round(Weapons.shiv['basePrice'] * buy_mod):
                        pc.gold_flakes -= round(Weapons.shiv['basePrice'] * buy_mod)
                        pc.inventory.append(Weapon(Weapons.shiv))
                    else:
                        print("\nYou don't have the money for this...")
                        Interface.pressEnter()
                elif userInput == "2":
                    if pc.gold_flakes >= round(Weapons.metal_pipe['basePrice'] * buy_mod):
                        pc.gold_flakes -= round(Weapons.metal_pipe['basePrice'] * buy_mod)
                        pc.inventory.append(Weapon(Weapons.metal_pipe))
                    else:
                        print("\nYou don't have the money for this...")
                        Interface.pressEnter()
                elif userInput == "3":
                    if pc.gold_flakes >= round(Weapons.bondprint_sabre['basePrice'] * buy_mod):
                        pc.gold_flakes -= round(Weapons.bondprint_sabre['basePrice'] * buy_mod)
                        pc.inventory.append(Weapon(Weapons.bondprint_sabre))
                    else:
                        print("\nYou don't have the money for this...")
                        Interface.pressEnter()

            elif userInput == "2":
                print("\n\nSorry, I'm all out of body armor...")
                Interface.pressEnter()
            elif userInput == "3":
                Interface.clear()
                print("\t--- [Merchant] ---\n")
                print("\n[Quartermaster Mathias]\n")
                print("What've you got?")
                print(f"\nInventory:")
                item_num = 0
                item_dict = {}
                for item in list(pc.inventory):
                    item_num += 1
                    item_dict[f"{item_num}"] = item
                    print(f"[{item_num}] {item.name} ({round(item.basePrice * sell_mod)} GF)")
                userInput = input("\n")
                if userInput in item_dict:
                    selected_item = item_dict[userInput]
                    userInput = input("\n[1] Sell\n\n")
                    if userInput == "1":
                        pc.gold_flakes += round(selected_item.basePrice * sell_mod)
                        pc.inventory.remove(selected_item)

            else:
                showMerchant = False


    def doctorMenu(pc):
        Interface.clear()
        print("\t--- [Doctor] ---\n")
        print("\n[Sr Researcher Lydia]\n")
        if pc.hp == pc.max_hp:
            print("You're healthy enough. Stop wasting my time!")
        elif pc.hp > pc.max_hp * 0.5:
            print("Not too bad, let me patch you up.")
        elif pc.hp > pc.max_hp * 0.25:
            print("You're not looking too hot...\nHave a seat and bite down on this.")
        elif pc.hp > 0:
            print("Set them down here! We'll start surgery immediately.")
        else:
            print(f"{pc.name} is dead...\nGet their body in the Anubis Chamber.")
        pc.hp = pc.max_hp
        Interface.pressEnter()


    def inventoryMenu(pc):
        inInventory = True
        while inInventory:
            Interface.clear()
            print("\t--- [Inventory] ---\n\n")
            Interface.characterInfo(pc, stats=False)
            if pc.inventory:
                print("\n[0] Switch to equipped")
                print(f"\nInventory:")
                item_num = 0
                item_dict = {}
                for item in list(pc.inventory):
                    item_num += 1
                    item_dict[f"{item_num}"] = item
                    print(f"[{item_num}] {item.name} ({item.durability})")
                userInput = input("\n")
                if userInput in item_dict:
                    selected_item = item_dict[userInput]
                    userInput = input("\n[1] Equip\n[2] Drop\n\n")
                    if userInput == "1":
                        if type(selected_item) is Weapon:
                            pc.equip_weapon(selected_item)
                        elif type(selected_item) is Wearable:
                            pc.equip_wearable(selected_item)
                    elif userInput == "2":
                        pc.inventory.remove(selected_item)
                    
                elif userInput == "0":
                    inEquipped = True
                    while inEquipped:
                        Interface.clear()
                        print("\t--- [Equipped] ---\n\n")
                        item_num = 0
                        item_dict = {}
                        if pc.equipped['mainHand']:
                            item_num += 1
                            print(f"Main-Hand: [{item_num}] {pc.equipped['mainHand'].name} ({item.durability})", end=" ")
                            item_dict[f"{item_num}"] = [pc.equipped['mainHand'], 'mainHand']
                        else:
                            print(f"Main-Hand: None", end=" ")

                        if pc.equipped['offHand']:
                            item_num += 1
                            print(f"| Off-Hand: [{item_num}] {pc.equipped['offHand'].name} ({item.durability})")
                            item_dict[f"{item_num}"] = [pc.equipped['offHand'], 'offhand']
                        else:
                            print(f"| Off-Hand: None")

                        print("Wearing: ", end="")
                        if pc.equipped['wearable']:
                            print("")
                            for item in pc.equipped['wearable']:
                                item_num += 1
                                print(f"[{item_num}] {item.name} ({item.durability})")
                                item_dict[f"{item_num}"] = [item, 'wearable']
                        else:
                            print("None")
                        
                        print("\n[0] Switch to inventory")

                        userInput = input("\n")
                        if userInput in item_dict:
                            selected_item = item_dict[userInput][0]
                            equip_type = item_dict[userInput][1]
                            userInput = input("\n[1] Unequip\n\n")
                            if userInput == "1":
                                if equip_type == "mainHand":
                                    pc.unequip_weapon(selected_item)
                                elif equip_type == "offHand":
                                    pass
                                elif equip_type == "wearable":
                                    pc.unequip_wearable(selected_item)
                        elif userInput == "0":
                            inEquipped = False
                        else:
                            inEquipped = False
                            inInventory = False
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
        