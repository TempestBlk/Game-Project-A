from entities import *
from operator import attrgetter

def random_encounter(pc):
    print("\n\n\n\n--------------[ Random Encounter ]--------------")
    turn_order = [pc] # list for combatants

    # building npcs
    npc_1 = PsyscarredHuman()
    npc_2 = PsyscarredHuman()
    npc_3 = PsyscarredHuman()

    npc_group = [npc_1, npc_2, npc_3] # grouping npcs
    turn_order += npc_group # adding npc group to combatants

    # pre-combat edits to npc stats
    npc_1.set_name("Psyscarred Human 1")
    npc_2.set_name("Psyscarred Human 2")
    npc_3.set_name("Psyscarred Human 3")
    npc_2.set_initiative(12)
    npc_3.set_initiative(7)

    in_combat = True
    downed_list = []
    round_num = 1
    while in_combat: # main combat loop
        print(f"\n\n[ ROUND {round_num} ]\n")
        if round_num == 15: # ending combat after x rounds
            in_combat = False
        turn_order.sort(key=attrgetter('initiative'), reverse=True) # re-sorts turn order at beginning of each round

        # NOTE: FOR TURN ORDER DEBUG
        '''
        print(f"\n[ DEBUG ] Current turn order -->")
        for entity in turn_order:
            print(f"{entity.get_name()}: {entity.get_initiative()}")
        '''
 
        turn_num = 1
        for entity in turn_order: # loop for running each turn in turn order
            print(f"Turn {turn_num}: ", end="")
            if type(entity) is not PlayerCharacter:
                if pc in turn_order:
                    target_list = [pc]
                else:
                    target_list = None
                print(f"{entity.get_name()}")
                newly_downed = entity.do_turn(target_list)
            else:
                target_list = npc_group # TODO: automatic enemy tracking
                print(f"{entity.get_name()}")
                newly_downed = pc.do_turn()
            if newly_downed is not None:
                if downed_list is not None:
                    downed_list = newly_downed
                else:
                    downed_list + newly_downed
                for entity in newly_downed:
                    turn_order.remove(entity)
            turn_num += 1
            print("")

        round_num += 1

    print("\DOWNED IN COMBAT:")
    for entity in downed_list:
        print(f"{entity.get_name()}")
    print("--------------[ Encounter Ended ]--------------\n\n")