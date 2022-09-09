from entities import PlayerCharacter, PsyscarredHuman
from operator import attrgetter
from debug import Debug

def random_encounter(pc):
    print("\n\n\n\n--------------[ Random Encounter ]--------------")
    combatants = [pc] # list for combatants

    # building npcs
    npc_1 = PsyscarredHuman()
    npc_2 = PsyscarredHuman()
    npc_3 = PsyscarredHuman()
    # pre-combat edits to npc stats
    npc_1.set_name("Psyscarred Human 1")
    npc_2.set_name("Psyscarred Human 2")
    npc_3.set_name("Psyscarred Human 3")
    npc_2.set_initiative(12)
    npc_3.set_initiative(7)
    npc_group = [npc_1, npc_2, npc_3] # grouping npcs
    combatants += npc_group # adding group to combatants

    downed_list = [] # downed entities are moved here from combatants
    round_num = 1
    in_combat = True # if true continues to the next round of combat
    while in_combat: # loops through rounds of combat
        print(f"\n\n[ ROUND {round_num} ]\n")
        combatants.sort(key=attrgetter('initiative'), reverse=True) # re-sorts turn order at beginning of each round

        # Debug.check_initiative(combatants)
 
        turn_num = 1
        for entity in combatants[:]: # loops through every combatant's turn in order of highest -> lowest initiative
            print(f"Turn {turn_num}: {entity.get_name()}")
            newly_downed = []
            
            if type(entity) is not PlayerCharacter:
                if pc in combatants: # FIXME: check if npcs can still target player (replace with check for any hostile combatants)
                    target_list = [pc]
                else:
                    target_list = None
            else: # if next extity is player
                target_list = npc_group # FIXME: add support for multiple combatant groups

            newly_downed = entity.do_turn(target_list)
            if newly_downed is not None: # check for newly downed combatants
                for entity in newly_downed:
                    downed_list.append(entity)
                    combatants.remove(entity)
            
            turn_num += 1
            print("")
            # end of turn

        if pc in downed_list or round_num == 15:
            in_combat = False
        else:
            round_num += 1
        # end of round

    # end of encounter
    print("DOWNED IN COMBAT:")
    for entity in downed_list:
        print(f"{entity.get_name()}")
    if pc in downed_list:
        print("\n--------------[ Encounter Failed ]--------------\n\n")
    else:
        print("\n--------------[ Encounter Completed ]--------------\n\n")