from entities import PlayerCharacter, PsyscarredHuman
from operator import attrgetter

class Encounter():
    def __init__(self, pc, enemies=[], allies=[]):
        self.encounter_id = 0
        self.pc = pc
        self.enemies = enemies
        self.allies = allies
        self.downed_list = [] # downed entities are added here
        self.turn_order = []


    def random_enemies(self):
        # building npcs
        npc_1 = PsyscarredHuman("Psyscarred Human 1")
        npc_2 = PsyscarredHuman("Psyscarred Human 2")
        npc_3 = PsyscarredHuman("Psyscarred Human 3")
        # building list of enemies
        self.enemies = [npc_1, npc_2, npc_3]


    def run_encounter(self):
        print("\n\n\n\n[Encounter] Running encounter.")
        if not self.enemies:
            self.random_enemies()

        # building turn order
        self.turn_order = [self.pc] + self.enemies # NOTE: use queue for turn_order?
        if self.allies:
            self.turn_order += self.allies

        round_num = 1
        in_combat = True
        while in_combat: # loops through rounds of combat
            print(f"\n\n[ROUND {round_num}]\n")
            self.turn_order.sort(key=attrgetter('initiative'), reverse=True) # re-sorts turn order at beginning of each round

            # Debug.check_initiative(combatants)
    
            turn_num = 1
            for entity in self.turn_order[:]: # loops through every combatant's turn in order of highest -> lowest initiative
                if entity not in self.downed_list: # ensuring entity isn't downed
                    print(f"Turn {turn_num}: {entity.get_name()}")
                    newly_downed = []
                    if type(entity) is PlayerCharacter:
                        target_list = self.enemies # FIXME: add support for multiple combatant groups
                    else: # if next extity is player
                        if self.pc in self.turn_order: # FIXME: check if npcs can still target player (replace with check for any hostile combatants)
                            target_list = [self.pc]
                        else:
                            target_list = None

                    newly_downed = entity.do_turn(target_list)
                    if newly_downed is not None: # check for newly downed combatants
                        for entity in newly_downed:
                            self.downed_list.append(entity)
                            self.turn_order.remove(entity)
                            if entity in self.enemies:
                                self.enemies.remove(entity)
                            elif entity in self.allies:
                                self.allies.remove(entity)
                
                turn_num += 1
                print("")
                # end of turn

            if self.pc in self.downed_list or not self.enemies or round_num == 15:
                in_combat = False
            else:
                round_num += 1
            # end of round

        # end of encounter
        print("[Encounter] Downed in combat:")
        for entity in self.downed_list:
            print(f"{entity.get_name()}")
        if self.pc in self.downed_list:
            print("\n[Encounter] Encounter failed, pc has fallen.\n\n")
        else:
            print("\n[Encounter] Encounter complete, all enemies have fallen.\n\n")