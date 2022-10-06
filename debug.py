# THIS FILE IS FOR TESTING AND DEBUGGING
from levels import Levels

class Debug():
    def check_pc(pc):
        lvlup_exp = Levels.lvl_dict[(pc.get_lvl() + 1)]
        print(f"\n{pc.get('name')}\nlevel: {pc.get_lvl()}\nexp: {pc.get_exp()}/{lvlup_exp}\nhp: {pc.get('hp')}/{pc.get('max_hp')}\nstatus: {pc.get('status')}\ninit: {pc.get('init')}/{pc.get('max_init')}")

    def check_init(combatants):
        print(f"\n[ DEBUG ] Current turn order -->")
        for entity in combatants:
            print(f"{entity.get('name')}: {entity.get('init')}")