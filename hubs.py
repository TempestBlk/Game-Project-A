from abc import ABCMeta, abstractmethod
import textwrap
from errors import QuitGame
from interface import Interface
from debug import Debug
from inventory import Inventory
from lifeforms import PlayerCharacter
from npcs import QuartermasterMathias, SeniorResearcherLydia
from gridmaps import PlayerGroup
from encounters import Encounter, EncounterBuilder


class Hub(metaclass=ABCMeta):
    """
    TODO:
    """

    title: str
    desc: str

    @abstractmethod
    def approach(pg) -> None:
        pass


    @abstractmethod
    def enter(pg) -> None:
        pass
    


class NorthWingSZ(Hub):
    """
    TODO:
    """
    
    title = "North Wing - Sealed Zone"
    desc = "An enclosed area in the north wing of Lab C1. Surviving personel took refuge here when the alarms went on. After a few days they ripped out speaker system, and sent a group to switch lights in the area to local power. Few returned, but they brought with them an outdated fabricator, crude weapons, and stories of creatures roaming the lab."
    
    @classmethod
    def hubHeader(self, pc:PlayerCharacter) -> None:
        Interface.clear()
        Interface.characterInfo(pc, equipped=False)
        print("\n")
        print(f"\t--- [ {self.title} ] ---\n")
        for line in textwrap.wrap(self.desc, 65):
            print(line)
        print("\n")


    @classmethod
    def approach(self, pg:PlayerGroup) -> None:
        self.enter(pg)


    @classmethod
    def enter(self, pg:PlayerGroup) -> None:
        inHub = True
        while inHub:
            self.hubHeader(pg.pc)
            userInput = input(f"[1] Explore (leave sealed zone)\n[2] Open Inventory\n[3] Approach the Quartermaster\n[4] Approach the Senior Researcher\n\n[R] Custom Encounter\n[P] See Protection Stats\n[X] Quit\n\n").lower()

            if userInput == "1":
                inHub = False
            elif userInput == "2":
                Inventory.open(pg.pc)
            elif userInput == "3":
                QuartermasterMathias.startDialogue(pg.pc)
            elif userInput == "4":
                SeniorResearcherLydia.startDialogue(pg.pc)
            elif userInput == "r":
                encounter = EncounterBuilder.build(pg.pc, difficulty_level=None)
                if isinstance(encounter, Encounter):
                    encounter.runEncounter()
            elif userInput == "p":
                Debug.showProtection(pg.pc)
            elif userInput == "x":
                raise QuitGame(pg.pc)