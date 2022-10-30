from attacks import Attack
from levelup import Levelup



class Lifeform(object):
    def __init__(self, name):
        self.name = name



class Humanoid(Lifeform):
    npcid = 0

    def __init__(self, name):
        self.npcid = Humanoid.npcid
        Humanoid.npcid += 1
        self.name = name
        self.max_hp = 16
        self.hp = self.max_hp
        self.max_init = 10
        self.init = self.max_init
        self.dodge_class = 10
        self.xp = 0
        self.level = 1
        self.xp_val = 10
        self.gold_flakes = 0
        self.unarmed = [Attack.fists_one_two]
        self.equipped = {
            "mainHand": None,
            "offHand": None,
            "wearable": None,
            }
        self.attacks = []
        for attack in list(self.unarmed):
            attack['givenBy'] = 'unarmed'
            self.attacks.append(attack)
        self.inventory = []
        self.protection = {
            'head': {'slash':0, 'pierce':0, 'blunt':0},
            'torso': {'slash':0, 'pierce':0, 'blunt':0},
            'stomach': {'slash':0, 'pierce':0, 'blunt':0},
            'arms': {'slash':0, 'pierce':0, 'blunt':0},
            'legs': {'slash':0, 'pierce':0, 'blunt':0},
            'hands': {'slash':0, 'pierce':0, 'blunt':0},
            'feet': {'slash':0, 'pierce':0, 'blunt':0},
            }
    

    def equip_weapon(self, weapon):
        current_weapon = self.equipped['mainHand']
        if current_weapon is not None:
            self.unequip_weapon(current_weapon, False)
        else:
            for attack in list(self.attacks):
                if attack['givenBy'] == 'unarmed':
                    self.attacks.remove(attack)

        if weapon in self.inventory:
            self.inventory.remove(weapon)

        self.equipped['mainHand'] = weapon
        for attack in weapon.attacks:
            attack['givenBy'] = weapon.name
            self.attacks.append(attack)


    def unequip_weapon(self, current_weapon, unarmed=True):
        for attack in list(self.attacks):
            if attack['givenBy'] == current_weapon.name:
                self.attacks.remove(attack)
        self.inventory.append(self.equipped['mainHand'])
        self.equipped['mainHand'] = None

        if unarmed:
            for attack in self.unarmed:
                self.attacks.append(attack)



class PlayerCharacter(Humanoid):
    def __init__(self, name, background):
        super().__init__(name)
        self.background = background
        self.xp_val = 0
    
    def addXp(self, value):
        self.xp += value
        Levelup.check(self)



class Mindless(Humanoid):
    def __init__(self, name):
        super().__init__(name)
        self.max_hp = 12
        self.hp = self.max_hp
        self.max_init = 8
        self.init = self.max_init
        self.dodge_class = 5
        self.xp_val = 8
        self.unarmed = [Attack.mindless_slam]
        self.attacks = []
        for attack in list(self.unarmed):
            attack['givenBy'] = 'unarmed'
            self.attacks.append(attack)