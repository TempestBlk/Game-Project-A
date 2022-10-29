from dice import Dice



class Attack():
    metal_pipe_slam = {
        "id": "metal_pipe_slam",
        "name": "Slam",
        "toHit": 12,
        "damage": [1,8,1],
        "damageType": "blunt",
        "twoHanded": True,
        }
    metal_pipe_swing = {
        "id": "metal_pipe_swing",
        "name": "Swing",
        "toHit": 14,
        "damage": [1,6,1],
        "damageType": "blunt",
        "twoHanded": False,
        }
    shiv_stab = {
        "id": "shiv_stab",
        "name": "Stab",
        "toHit": 14,
        "damage": [1,4,1],
        "damageType": "pierce",
        "twoHanded": False
        }
    fists_one_two = {
        "id": "fists_one_two",
        "name": "One-two",
        "toHit": 12,
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

        target.hp -= damage
        report.turn_report += f"\n--> Hit! Dealt {damage} damage.{log}"
        
        downed = []
        if target.hp <= 0:
            report.turn_report += f"\n--> {target.name} died!"
            downed.append(target)
        return downed