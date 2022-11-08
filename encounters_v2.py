import random
from dice import Dice
from lifeforms import Lifeform, Mindless, Humanoid, PlayerCharacter
from attacks import Attack
from interface import Interface
from items import Weapon



class Difficulty():
    
    # NOTE: list[list[lifeform, name, main_hand_weapon]]
    LIGHT = [
        [[Mindless, "Mindless-1"]],
        [[Humanoid, "Vagrant-1"]]
    ]
    AVERAGE = [
        [[Humanoid, "Vagrant-1", Weapon.shiv]],
        [[Mindless, "Mindless-1"], [Mindless, "Mindless-2"]]
    ]
    DIFFICULT = [
        [[Humanoid, "Vagrant-1", Weapon.metal_pipe], [Humanoid, "Vagrant-2", Weapon.shiv]],
        [[Mindless, "Mindless-1", Weapon.metal_pipe], [Mindless, "Mindless-1"], [Mindless, "Mindless-1"]]
    ]



class EncounterReporter(object):

    def __init__(self) -> None:
        self.round_count = 0
        self.round_border = "\n\n-----------------------------"


    def roundTitle(self, round_count:int) -> str:
        round_title = f"\n\n\t[Round {round_count}]"
        self.round_count += 1
        return round_title


    def actorInfo(actor:Lifeform):
        pass



class EncounterBuilder():

    def options(pc:PlayerCharacter, allies:list[Lifeform]=[]) -> None:
        if pc.hp < 0:
            print(f"\n{pc.name} is dead...")
            return Interface.pressEnter()

        Interface.clear()
        userInput = input("\nChoose a difficulty.\n[1] Light\n[2] Average\n[3] Difficult\n\n[Enter] Go Back\n\n")
        difficulty_dict = {"1": Difficulty.LIGHT, "2": Difficulty.AVERAGE, "3": Difficulty.DIFFICULT}
        if userInput not in difficulty_dict:
            return Interface.pressEnter()
        
        difficulty = difficulty_dict[userInput]
        scenario = random.choice(difficulty)
        
        enemies = []
        for enemy in scenario:
            enemy_class = enemy[0]
            lifeform:Lifeform = enemy_class(enemy[1])
            if len(enemy) > 2:
                lifeform.equipWeapon(Weapon(enemy[2]))
            enemies.append(lifeform)
        
        Encounter(pc, enemies, allies)



class Actor():

    def __init__(self, lifeform:Lifeform, group:list[Lifeform], hostiles:list[Lifeform]) -> None:
        self.lifeform = lifeform
        self.group = group
        self.hostiles = hostiles



class Encounter():

    def __init__(self, pc:PlayerCharacter, enemies:list[Lifeform], allies:list[Lifeform]=[]) -> None:
        self.pc = pc
        self.allies = allies + [pc]
        self.enemies = enemies

        self.combatants = self.buildActors()
        self.turn_order:list[Actor]
        self.sortTurnOrder()
        self.recorder = EncounterReporter()

        self.player_xp = 0
        self.inCombat = True
        self.runEncounter()


    def buildActors(self) -> list[Actor]:
        combatants = []
        for lifeform in self.allies:
            combatants.append(Actor(lifeform, self.allies, self.enemies))
        for lifeform in self.enemies:
            combatants.append(Actor(lifeform, self.enemies, self.allies))
        return combatants

    
    def sortTurnOrder(self) -> None:
        self.turn_order = sorted(self.combatants, key=lambda x: x.lifeform.init, reverse=True)

    
    def removeActor(self, target:Lifeform) -> None:
        for actor in self.combatants:
            if actor.lifeform is target:
                actor.group.remove(target)
                self.combatants.remove(actor)


    def doAttack(self, target:Lifeform, attack:Attack) -> None:
        toHit = Dice.roll([1,20,attack["toHit"]])
        toHit = toHit//2
        if toHit < target.dodge_class:
            return
        
        damage_reduction:int = target.protection['torso'][attack['damageType']] // 5
        protection = damage_reduction // 2

        for item in list(target.equipped['wearable']): # TODO: check for item break
            item.durability -= 1

        if (protection + target.dodge_class) > toHit:
            return

        damage = Dice.roll(attack['damage']) # TODO: attack.givenby loses durability

        if damage_reduction == 0:
            target.hp -= damage
        elif damage == 1:
            return
        elif damage_reduction >= damage:
            target.hp -= 1
        else:
            target.hp -= (damage - damage_reduction)

        if target.hp <= 0:
            self.removeActor(target)
            

    
    def doTurn(self, actor:Actor) -> None:
        if not actor.hostiles:
            return
        action_decider = random.randint(1, 5)
        if action_decider == 0:
            return
        target = random.choice(actor.hostiles)
        attack = random.choice(actor.lifeform.attacks)
        self.doAttack(actor, target, attack)


    def runEncounter(self) -> None:
        Interface.encounterStart()
        while self.inCombat:
            while self.turn_order:
                self.sortTurnOrder()
                actor = self.turn_order[0]
                self.doTurn(actor)
                self.turn_order.remove(actor)
            
            if not self.enemies:
                self.in_combat = False
                
