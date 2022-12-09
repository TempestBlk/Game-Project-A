import os
from lifeforms import Lifeform, PlayerCharacter


class Interface:
    """
    TODO:
    """

    @staticmethod
    def clear() -> None:
        clear = lambda: os.system('cls')
        clear()


    @staticmethod
    def pressEnter() -> None:
        input("\n\nPress Enter to continue... ")
        Interface.clear()


    @staticmethod
    def alert(msg) -> None:
        Interface.clear()
        print(msg)
        Interface.pressEnter()


    @staticmethod
    def notImplemented() -> None:
        Interface.alert("\t---[ Not implemented ]---\n\nTry again later.\n\n")


    @staticmethod
    def startup() -> None:
        Interface.clear()
        print("--------------[ Turn-Based Combat ]--------------")
        Interface.pressEnter()
    

    @staticmethod
    def shutdown() -> None:
        print("\n--------------[ Shutting Down ]--------------")
        Interface.pressEnter()


    @staticmethod
    def characterInfo(pc:PlayerCharacter, stats=True, equipped=True) -> None:
        if stats:
            print(f"\n[ {pc.name} ]\nHp: {pc.hp}/{pc.max_hp} | Level: {pc.level} | Xp: {pc.xp}\nInitiative: {pc.init} | Dodge Class: {pc.dodge_class}\nGold Flakes: {pc.gold_flakes}")
        if equipped:
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

    
    @staticmethod
    def levelupMessage(lifeform:Lifeform):
        Interface.clear()
        print(f"\t--- [ Levelup ] ---")
        print(f"\n{lifeform.name} has reached experience level {lifeform.level}!")
        Interface.pressEnter()
    

    @staticmethod
    def encounterStart():
        Interface.clear()
        print(f"\t--- [Encounter Starting] ---")
        Interface.pressEnter()
    

    @staticmethod
    def error01():
        print("\n\n[ERROR-01] Encounter cant handle unaffiliated yet.")
        Interface.pressEnter()
    

    @staticmethod
    def error02():
        print("\n\n[ERROR-02] Include difficulty when building encounter.")
        Interface.pressEnter()


    @staticmethod
    def error03():
        print("\n\n[ERROR-03] Encounter difficulty level is invalid.")
        Interface.pressEnter()