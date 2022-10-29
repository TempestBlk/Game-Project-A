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



class Reporter():
    def __init__(self):
        self.round_counter = 1
        self.turn_counter = 1
        self.nextRound()
    
    def nextRound(self):
        self.round_report = "\n\n-----------------------------"
        self.turn_report = ""

    def print(self):
        self.turn_report += "\n\n-----------------------------"
        print(self.round_report + self.turn_report)
        self.round_report = "\n\n-----------------------------"
        self.turn_report = ""




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


    def doTurn(self, report, actor, target_list=False):
        if not target_list:
            report.turn_report += "\n--> Waits..."
            return None

        action_decider = random.randint(1, 5)
        if action_decider == 0:
            report.turn_report += "\n--> Waits..."
            return None
        
        target = random.choice(target_list)
        attack = random.choice(actor.attacks)
        report.turn_report += f"\n--> Attacks {target.name} with {attack['name']}."
        
        downed_list = []
        downed = Attack.single_target(report, actor, target, attack)
        downed_list += downed
        return downed_list


    def start(self):
        self.buildCombatants()
        Interface.encounterStart()
        report = Reporter()
        
        while self.in_combat:
            report.round_report += f"\n\n\t[Round {report.round_counter}]"
            report.round_counter += 1

            self.turn_order = sorted(self.combatants, key=lambda x: x.init, reverse=True)
            
            while len(self.turn_order) > 0:
                actor = self.turn_order[0]
                if actor in self.allies:
                    target_list = self.enemies
                elif actor in self.enemies:
                    target_list = self.allies + [self.pc]
                else:
                    return Interface.error01()
                
                report.turn_report += f"\n\nTurn {report.turn_counter} : {actor.name}"
                report.turn_counter += 1

                downed_list = self.doTurn(report, actor, target_list)
                
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
            
            Interface.characterInfo(self.pc)
            
            report.print()

            if not self.enemies:
                self.in_combat = False
            Interface.pressEnter()
        
        print(f"\n\t--- [Encounter Ended] ---\n")
        
        if self.pc not in self.combatants:
            print(f"{self.pc.name} has fallen in battle!")
        else:
            print(f"{self.pc.name} gained {self.player_xp} xp.")
            self.pc.xp += self.player_xp

        if self.all_downed:
            print(f"\nDowned:")
            for lifeform in self.all_downed:
                print(f"- {lifeform.name}")
        
        Interface.pressEnter()
            