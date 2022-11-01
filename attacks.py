from dice import Dice



class Attack():
    metal_pipe_slam = {
        "id": "metal_pipe_slam",
        "name": "Slam",
        "toHit": 10,
        "damage": [1,8,1],
        "damageType": "blunt",
        "twoHanded": True,
        }
    metal_pipe_swing = {
        "id": "metal_pipe_swing",
        "name": "Swing",
        "toHit": 12,
        "damage": [1,6,1],
        "damageType": "blunt",
        "twoHanded": False,
        }
    shiv_stab = {
        "id": "shiv_stab",
        "name": "Stab",
        "toHit": 12,
        "damage": [1,4,1],
        "damageType": "pierce",
        "twoHanded": False
        }
    fists_one_two = {
        "id": "fists_one_two",
        "name": "One-two",
        "toHit": 10,
        "damage": [1,4,0],
        "damageType": "blunt",
        "twoHanded": True
        }
    mindless_slam = {
        "id": "mindless_slam",
        "name": "Slam",
        "toHit": 8,
        "damage": [1,4,1],
        "damageType": "blunt",
        "twoHanded": False
        }
    bondprint_sabre_slash = {
        "id": "bondprint_sabre_slash",
        "name": "Slash",
        "toHit": 14,
        "damage": [2,4,1],
        "damageType": "slash",
        "twoHanded": False
    }
    bondprint_sabre_cleave = {
        "id": "bondprint_sabre_cleave",
        "name": "Slash",
        "toHit": 12,
        "damage": [2,6,0],
        "damageType": "slash",
        "twoHanded": True
    }
    f_collective_solspear_impale = {
        "id": "f_collective_solspear_impale",
        "name": "Impale",
        "toHit": 16,
        "damage": [2,8,1],
        "damageType": "pierce",
        "twoHanded": True
    }


    def single_target(report, actor, target, attack, logging=False, printing=False):
        if logging:
            toHit, log = Dice.roll([1,20,attack["toHit"]], logging=True, printing=printing)
            log = f" [ ({log}) // 2 = {toHit} < {target.dodge_class} ]"
        else:
            toHit = Dice.roll([1,20,attack["toHit"]])
            log = ""

        toHit = toHit//2
        if toHit < target.dodge_class:
            report.turn_report += f"\n--> Misses!{log}"
            return []

        if logging:
            damage, log = Dice.roll(attack['damage'], logging=True, printing=printing)
            log = f" [ {log} = {damage} ]"
        else:
            damage = Dice.roll(attack['damage'], logging=False, printing=printing)
            log = ""

        # TODO:
        # attack.givenby loses durability
        
        protection = target.protection['torso'][f"{attack['damageType']}"] // 10
        damage_reduction = 0

        if (protection + target.dodge_class) > toHit:
            report.turn_report += f"\n--> Absorbed by armor!"

            for item in list(target.equipped['wearable']): # NOTE: check for break
                item.durability -= 1

            return []
        else:
            damage_reduction = protection * 2

        if damage_reduction == 0:
            target.hp -= damage
            report.turn_report += f"\n--> Hit! Dealt {damage} damage.{log}"
        else:
            min_damage = 1
            if damage == 1:
                min_damage = 0
            if damage_reduction >= damage:
                damage_reduction = damage - min_damage
                
            reduced_damage = (damage - damage_reduction)
            target.hp -= reduced_damage
            report.turn_report += f"\n--> Hit! Armor absorbed {damage_reduction} damage. Dealt {reduced_damage}. {log}"
        
        for item in list(target.equipped['wearable']): # NOTE: check for break
            item.durability -= 1
        
        downed = []
        if target.hp <= 0:
            report.turn_report += f"\n--> {target.name} died!"
            downed.append(target)
        return downed