#  Entity Collection
#
# NOTE: possible entity save feature for reintroducing enemies that got away with flags to make them familiar

import random
from dice import Dice
from menu import Menu
from attacks import Attacks
from levels import Levels

# TODO: implement stamina/wind, inventory/equipped

class Entity():
# CONSTRUCTOR - Entity
    def __init__(self, name, max_hp, hp, max_init, init, ac):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.max_init = max_init
        self.init = init
        self.ac = ac
        self.status = []
        self.atks = []
        self.equipped = []
        self.inventory = []
    
# GET method
    def get(self, prop):
        if prop == "max_hp":
            return self.max_hp
        elif prop == "hp":
            return self.hp
        elif prop == "name":
            return self.name
        elif prop == "max_init":
            return self.max_init
        elif prop == "init":
            return self.init
        elif prop == "ac":
            return self.ac
        elif prop == "status":
            return self.status
        elif prop == "atks":
            return self.atks
        elif prop == "equipped":
            return self.equipped

# SET method
    def set(self, prop, value):
        if prop == "name":
            self.name = value
        elif prop == "hp":
            self.hp = value
        elif prop == "init":
            self.init = value
        elif prop == "atks":
            self.atks = value

# COMBAT methods
    def add_atk(self, atk):
        self.atks += [atk]
    def add_status(self, status):
        self.status.append(status)
    def rm_status(self, status):
        if status in self.status:
            self.status.remove(status)
        else:
            print(f"[ERROR] Status to remove not found.")
    def take_atk(self, atk):
        # NOTE: for when attacks become more complicated
        pass
    def take_dmg(self, dmg, dmgType):
        self.hp -= dmg
    def do_atk(self, atk, target):
        newly_downed = []
        to_hit = Dice.roll([1, 20, atk['hitMod']])
        if to_hit < target.get('ac'):
            print(f"- missed {target.get('name')} with {atk['name']}")
            return
        else:
            dmg = Dice.roll(atk['dmgRoll'])
            target.take_dmg(dmg, atk['dmgType'])
            print(f"- hit {target.get('name')} with {atk['name']} dealing {dmg} damage")
            print(f"- {target.get('name')} has {target.get('hp')} hp left")
        if target.get('hp') <= 0:
            print(f"- {target.get('name')} has been downed!")
            target.add_status('downed')
            newly_downed.append(target)
        return newly_downed
        

class PlayerCharacter(Entity):
# CONSTRUCTOR - Player Character
    def __init__(self, name="Player", max_hp=60, hp=60, max_init=10, init=10, ac=10):
        super().__init__(name, max_hp, hp, max_init, init, ac)
        self.add_atk(Attacks.atk_dict["Fists"])
        self.add_atk(Attacks.atk_dict["Annihilate"])
        self.exp = 0
        self.lvl = 1
    
# GET method
    def get(self, prop):
        return super().get(prop)

# SET method
    def set(self, prop, value):
        super().set(prop, value)

# COMBAT methods
    def add_atk(self, atk):
        return super().add_atk(atk)
    def add_status(self, status):
        return super().add_status(status)
    def rm_status(self, status):
        return super().rm_status(status)
    def take_dmg(self, dmg, dmgType):
        return super().take_dmg(dmg, dmgType)
    def do_turn(self, target_list):
        downed_list = []
        target = target_list[int(Menu.option_menu("Choose a target.", target_list)) - 1]
        atks = self.atks
        atk = atks[int(Menu.option_menu("Choose an attack.", atks)) - 1]
        newly_downed = self.do_atk(atk, target)
        if newly_downed is not None:
            downed_list += newly_downed
        return downed_list

# PlayerCharacter specific methods
    def get_exp(self):
        return self.exp
    def add_exp(self, exp):
        self.exp += exp
    def set_exp(self, exp):
        self.exp = exp
    def get_lvl(self):
        return self.lvl
    def add_lvl(self):
        self.lvl += 1
    def set_lvl(self, lvl):
        self.lvl = lvl


class PsyscarredHuman(Entity):
# CONSTRUCTOR - Psyscarred Human
    def __init__(self, name="Psyscarred Human", max_hp=50, hp=50, max_init=8, init=8, ac=8):
        super().__init__(name, max_hp, hp, max_init, init, ac)
        super().set("atks", [
            {
            'name': 'Slam',
            'hitMod': 0,
            'dmgRoll': [3, 4, 1],
            'dmgType': 'blugeoning'
            }
        ])

# GET method
    def get(self, prop):
        return super().get(prop)

# SET method
    def set(self, prop, value):
        super().set(prop, value)

# COMBAT methods
    def add_status(self, status):
        return super().add_status(status)
    def rm_status(self, status):
        return super().rm_status(status)
    def take_dmg(self, dmg, dmgType):
        return super().take_dmg(dmg, dmgType)
    def do_atk(self, atk, target):
        return super().do_atk(atk, target)
    def do_turn(self, target_list):
        downed_list = []
        action_num = random.randint(1, 4)
        if target_list is not None and action_num in [1, 2, 3]:
            if len(target_list) == 1:
                target = target_list[0]
            else:
                target_num = random.randint(1, len(target_list))
                target = target_list[target_num - 1]
            atks = self.atks
            if len(atks) == 1:
                atk = atks[0]
            else:
                atk_num = random.randint(1, len(atks))
                atk = atks[atk_num - 1]
            newly_downed = self.do_atk(atk, target)
            if newly_downed is not None:
                downed_list += newly_downed
            return downed_list
        else:
            print("- twitches and mutters...")