import random
from lifeforms import Mindless, Humanoid
from attacks import Attack
from interface import Interface



class Encounters():
    eid = 0

    easy_encounters = [
        [["mindless","Mindless-1"]],
        [["humanoid","Vagrant-1"]],
        ]
    medium_encounters = [
        [["humanoid","Vagrant-1"]],
        [["mindless","Mindless-1"], ["mindless","Mindless-2"]]
        ]
    hard_encounter = []


    def buildEnemies(enemies, difficulty):
        if difficulty == 1:
            scenario = random.choice(list(Encounters.easy_encounters))
        elif difficulty == 2:
            scenario = random.choice(list(Encounters.medium_encounters))
        else:
            Interface.error03()
        
        for enemy in scenario:
            if enemy[0] == "humanoid":
                humanoid = Humanoid(enemy[1])
                enemies.append(humanoid)
            elif enemy[0] == "mindless":
                mindless = Mindless(enemy[1])
                enemies.append(mindless)
        return enemies



class Encounter(Encounters):
    def __init__(self, pc, difficulty=None, allies=[], unaffiliated=[]):
        self.eid = Encounters.eid
        Encounter.eid += 1

        self.pc = pc
        self.combatants = [self.pc]
        self.allies = list(allies)
        self.enemies = []
        self.unaffiliated = list(unaffiliated)
        self.difficulty = difficulty

        if self.difficulty is None:
            return Interface.error02()
        if self.difficulty in [1,2]:
            self.enemies = Encounters.buildEnemies(self.enemies, self.difficulty)
        else:
            return Interface.error03

        self.all_downed = []
        self.player_xp = 0
        self.in_combat = True
        self.start()


    def buildCombatants(self):
        self.combatants += self.enemies
        self.combatants += self.allies
        self.allies += [self.pc]
        self.combatants += self.unaffiliated


    def start(self):
        self.buildCombatants()
        Interface.encounterStart()
        reporter = Reporter()
        
        while self.in_combat:
            reporter.nextRound()

            self.turn_order = sorted(self.combatants, key=lambda x: x.init, reverse=True)
            
            while len(self.turn_order) > 0:
                actor = self.turn_order[0]
                if actor in self.allies:
                    target_list = self.enemies
                elif actor in self.enemies:
                    target_list = self.allies + [self.pc]
                else:
                    return Interface.error01()
                
                downed_list = self.doTurn(reporter, actor, target_list)

                if downed_list:
                    if actor is self.pc:
                        for lifeform in downed_list:
                            self.player_xp += lifeform.xp_val

                    for lifeform in downed_list:
                        self.combatants.remove(lifeform)
                        self.all_downed.append(lifeform)
                        if lifeform in self.turn_order:
                            self.turn_order.remove(lifeform)
                        
                        if lifeform is self.pc:
                            self.in_combat = False
                        elif lifeform in self.enemies:
                            self.enemies.remove(lifeform)
                        elif lifeform in self.allies:
                            self.allies.remove(lifeform)
                        elif lifeform in self.unaffiliated:
                            self.unaffiliated.remove(lifeform)

                self.turn_order.remove(actor)
                self.turn_order.sort(reverse=True, key=lambda x: x.init)

            if not self.enemies:
                self.in_combat = False

            Interface.characterInfo(self.pc)
            reporter.print()
            Interface.pressEnter()
        
        Interface.encounterEnd(self)
        self.pc.addXp(self.player_xp)


    def doTurn(self, reporter, actor, target_list=False):
        reporter.nextTurn(actor)
        
        if not target_list:
            reporter.turn_report += "\n--> Waits..."
            return None

        action_decider = random.randint(1, 5)
        if action_decider == 0:
            reporter.turn_report += "\n--> Waits..."
            return None
        
        target = random.choice(target_list)
        attack = random.choice(actor.attacks)
        reporter.turn_report += f"\n--> Attacks {target.name} with {attack['name']}."
        
        downed_list = []
        downed = Attack.single_target(reporter, actor, target, attack)
        downed_list += downed
        return downed_list



class Reporter():
    def __init__(self):
        self.round_counter = 1
        self.turn_counter = 1
        self.reset()


    def reset(self):
        self.round_report = "\n\n-----------------------------"
        self.turn_report = ""
    

    def nextRound(self):
        self.round_report += f"\n\n\t[Round {self.round_counter}]"
        self.round_counter += 1


    def nextTurn(self, actor):
        if actor.hp > actor.max_hp / 2:
           actor_health = "Healthy"
        elif actor.hp > actor.max_hp / 4:
            actor_health = "Bloodied"
        else:
            actor_health = "Dying"

        self.turn_report += f"\n\nTurn {self.turn_counter} : {actor.name} | {actor_health}"
        self.turn_counter += 1


    def print(self):
        self.turn_report += "\n\n-----------------------------"
        print(self.round_report + self.turn_report)
        self.reset()