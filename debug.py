from lifeforms import Humanoid



class Debug():
    def show_attacks(humanoid):
        print(f"\n[ {humanoid.name} ]\nmainHand: {humanoid.equipped['mainHand']} | offHand: {humanoid.equipped['offHand']} | wearable: {humanoid.equipped['wearable']}")
        print("attacks:")
        for attack in humanoid.attacks:
            print(f"\tname: {attack['name']} | givenBy: {attack['givenBy']}")
        print("inventory:")
        for item in humanoid.inventory:
            print(f"\tname: {item.name} | durability: {item.durability}")


    def test_npcid():
        npc1 = Humanoid("name")
        npc2 = Humanoid("name")
        npc3 = Humanoid("name")
        print(f"\t\t{npc1.npcid} | {npc2.npcid} | {npc3.npcid}")