#  Entity Collection
#
# NOTE: possible entity save feature for reintroducing enemies that got away with flags to make them familiar

import random
from dice import Dice
from menu import Menu

# TODO: implement stamina/wind/resevoir, inventory/equipped

class Entity():
# CONSTRUCTOR - Entity
    def __init__(self, name, max_hp, hp, initiative, ac):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.status = []
        self.initiative = initiative
        self.ac = ac
        self.atk_list = [
            {
            'name': 'Fists',
            'hitMod': 0,
            'dmgRoll': [2, 4, 1],
            'dmgType': 'blugeoning'
            }
        ]
    
    # GET methods
    def get_max_hp(self):
        return self.max_hp
    def get_hp(self):
        return self.hp
    def get_name(self):
        return self.name
    def get_initiative(self):
        return self.initiative
    def get_ac(self):
        return self.ac
    def get_status(self):
        return self.status
    def get_atk_list(self):
        return self.atk_list

    # SET methods
    def set_hp(self, hp):
        self.hp = hp
    def set_name(self, name):
        self.name = name
    def set_initiative(self, initiative):
        self.initiative = initiative
    def set_atk_list(self, atk_list):
        self.atk_list = atk_list

    # COMBAT methods
    def add_atk(self, atk):
        self.atk_list += atk
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
        if to_hit < target.get_ac():
            print(f"- missed {target.get_name()} with {atk['name']}")
            return
        else:
            dmg = Dice.roll(atk['dmgRoll'])
            target.take_dmg(dmg, atk['dmgType'])
            print(f"- hit {target.get_name()} with {atk['name']} dealing {dmg} damage")
            print(f"- {target.get_name()} has {target.get_hp()} hp left")
        if target.get_hp() <= 0:
            print(f"- {target.get_name()} has been downed!")
            target.add_status('downed')
            newly_downed.append(target)
        return newly_downed
        

class PlayerCharacter(Entity):
# CONSTRUCTOR - Player Character
    def __init__(self, name="Player"):
        max_hp = 60
        hp = 60
        initiative = 10
        ac = 10
        super().__init__(name, max_hp, hp, initiative, ac)
        super().add_atk([
            {
            'name': 'Annihilate',
            'hitMod': 10,
            'dmgRoll': [5, 10, 10],
            'dmgType': 'superluminal'
            }
        ])
    
    # GET methods
    def get_hp(self):
        return super().get_hp()
    def get_name(self):
        return super().get_name()
    def get_initiative(self):
        return super().get_initiative()
    def get_ac(self):
        return super().get_ac()
    def get_status(self):
        return super().get_status()
    def get_atk_list(self):
        return super().get_atk_list()

    # SET methods
    def set_hp(self, hp):
        return super().set_hp(hp)
    def set_name(self, name):
        return super().set_name(name)
    def set_initiative(self, initiative):
        return super().set_initiative(initiative)

    # COMBAT methods
    def add_status(self, status):
        return super().add_status(status)
    def rm_status(self, status):
        return super().rm_status(status)
    def take_dmg(self, dmg, dmgType):
        return super().take_dmg(dmg, dmgType)
    def do_turn(self, target_list):
        downed_list = []
        target = target_list[int(Menu.option_menu("Choose a target.", target_list)) - 1]
        atk_list = self.atk_list
        atk = atk_list[int(Menu.option_menu("Choose an attack.", atk_list)) - 1]
        newly_downed = self.do_atk(atk, target)
        if newly_downed is not None:
            downed_list += newly_downed
        return downed_list

        # newly_downed = self.do_atk(atk, target)
        # if newly_downed is not None:
        #     newly_downed += newly_downed
        # return newly_downed

class PsyscarredHuman(Entity):
# CONSTRUCTOR - Psyscarred Human
    def __init__(self, name="Psyscarred Human"):
        max_hp = 50
        hp = 50
        initiative = 8
        ac = 8
        super().__init__(name, max_hp, hp, initiative, ac)
        super().set_atk_list([
            {
            'name': 'Slam',
            'hitMod': 0,
            'dmgRoll': [3, 4, 1],
            'dmgType': 'blugeoning'
            }
        ])

    # GET methods
    def get_hp(self):
        return super().get_hp()
    def get_name(self):
        return super().get_name()
    def get_initiative(self):
        return super().get_initiative()
    def get_ac(self):
        return super().get_ac()
    def get_status(self):
        return super().get_status()
    def get_atk_list(self):
        return super().get_atk_list()

    # SET methods
    def set_hp(self, hp):
        return super().set_hp(hp)
    def set_name(self, name):
        return super().set_name(name)
    def set_initiative(self, initiative):
        return super().set_initiative(initiative)

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
            atk_list = self.atk_list
            if len(atk_list) == 1:
                atk = atk_list[0]
            else:
                atk_num = random.randint(1, len(atk_list))
                atk = atk_list[atk_num - 1]
            newly_downed = self.do_atk(atk, target)
            if newly_downed is not None:
                downed_list += newly_downed
            return downed_list
        else:
            print("- twitches and mutters...")