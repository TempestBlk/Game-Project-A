# THIS FILE IS FOR TESTING AND DEBUGGING

class Debug():
    def check_pc(pc):
        print(f"\n{pc.get_name()}\nhp: {pc.get_hp()}\nstatus: {pc.get_status()}")

    def check_initiative(combatants):
        print(f"\n[ DEBUG ] Current turn order -->")
        for entity in combatants:
            print(f"{entity.get_name()}: {entity.get_initiative()}")