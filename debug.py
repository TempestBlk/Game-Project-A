from lifeforms import Humanoid
from interface import Interface


class Debug():

    @staticmethod
    def showAttacks(humanoid:Humanoid):
        print(f"\n[ {humanoid.name} ]\nmainHand: {humanoid.equipped['mainHand']} | offHand: {humanoid.equipped['offHand']} | wearable: {humanoid.equipped['wearable']}")
        print("attacks:")
        for attack in humanoid.attacks:
            print(f"\tname: {attack['name']} | givenBy: {attack['givenBy']}")
        print("inventory:")
        for item in humanoid.inventory:
            print(f"\tname: {item.name} | durability: {item.durability}")


    @staticmethod
    def testNpcid():
        npc1 = Humanoid("name")
        npc2 = Humanoid("name")
        npc3 = Humanoid("name")
        print(f"\t\t{npc1.npcid} | {npc2.npcid} | {npc3.npcid}")

    
    @staticmethod
    def showProtection(humanoid:Humanoid):
        Interface.clear()
        print("\t---[ Protection Values by Body Part ]---\n\n")
        Interface.characterInfo(humanoid, stats=False)
        print("\n")
        for body_part in humanoid.protection:
            print(f"{str(body_part).title()} -> {humanoid.protection[body_part]}")
        Interface.pressEnter()