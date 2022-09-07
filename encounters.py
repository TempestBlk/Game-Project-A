from entities import PlayerCharacter, PsyscarredHuman
from operator import attrgetter

def random_encounter(pc):
    print("\n\n\n\n--------------[ Random Encounter ]--------------")
    combatants = [pc] # list for combatants

    # building npcs
    npc_1 = PsyscarredHuman()
    npc_2 = PsyscarredHuman()
    npc_3 = PsyscarredHuman()

    npc_group = [npc_1, npc_2, npc_3] # grouping npcs
    combatants += npc_group # adding npc group to combatants

    # pre-combat edits to npc stats
    npc_1.set_name("Psyscarred Human 1")
    npc_2.set_name("Psyscarred Human 2")
    npc_3.set_name("Psyscarred Human 3")
    npc_2.set_initiative(12)
    npc_3.set_initiative(7)

    in_combat = True # if true continues to the next round of combat
    downed_list = [] # downed entities are moved here from combatants
    round_num = 1
    while in_combat: # loops through rounds of combat
        print(f"\n\n[ ROUND {round_num} ]\n")
        if round_num == 15: # FOR TESTING: ending combat after x rounds
            in_combat = False
        combatants.sort(key=attrgetter('initiative'), reverse=True) # re-sorts turn order at beginning of each round

        ''' # NOTE: FOR TURN ORDER DEBUG
        print(f"\n[ DEBUG ] Current turn order -->")
        for entity in combatants:
            print(f"{entity.get_name()}: {entity.get_initiative()}")
        '''
 
        turn_num = 1
        for entity in combatants: # loops through every combatant's turn in order of highest -> lowest initiative
            print(f"Turn {turn_num}: ", end="")
            if type(entity) is not PlayerCharacter:
                if pc in combatants: # NOTE: check if npcs can still target player (replace with check for any hostile combatants)
                    target_list = [pc]
                else:
                    target_list = None
                print(f"{entity.get_name()}")
                newly_downed = entity.do_turn(target_list)
            else: # if next extity is player
                target_list = combatants # TODO: add support for multiple combatant groups
                print(f"{entity.get_name()}")
                newly_downed = pc.do_turn(target_list)

            if newly_downed is not None: # check for newly downed combatants
                if downed_list is not None:
                    downed_list = newly_downed
                else:
                    downed_list + newly_downed
                for entity in newly_downed:
                    combatants.remove(entity)
            
            turn_num += 1
            print("")
            # end of turn
        
        if pc in downed_list:
            in_combat = False
        else:
            round_num += 1
        # end of round

    # end of encounter
    print("DOWNED IN COMBAT:")
    for entity in downed_list:
        print(f"{entity.get_name()}")
    if pc in downed_list:
        print("--------------[ Encounter Failed ]--------------\n\n")
    else:
        print("--------------[ Encounter Completed ]--------------\n\n")