import random
from abc import ABCMeta, abstractmethod
from errors import QuitGame
from interface import Interface
from items import Weapon
from lifeforms import Lifeform, PlayerCharacter, Mindless
from encounters import EncounterBuilder


class Gridsquare:
    """
    A Gridsquare is created for every coordinate point in its Gridmap.\n
    May contain a MapEntity.
    """

    def __init__(self, coords:tuple, within:object) -> None:
        self.coords = coords
        self.within = within

    
class Gridmap:
    """
    Data structure containing a two dimensional grid of Gridsquares.\n
    Handles displaying map in terminal.
    """

    UP = (0,-1)
    LEFT = (-1,0)
    DOWN = (0,1)
    RIGHT = (1,0)

    mapping: dict[tuple, Gridsquare]

    def __init__(self, width:int, height:int) -> None:
        self.width = width
        self.height = height
        self.mapping = {}
        for y in range(height):
            for x in range(width):
                gsquare = Gridsquare((x,y), None)
                self.mapping[(x,y)] = gsquare


    def display(self) -> None:
        for y in range(self.height):
            print("")
            for x in range(self.width):
                end = " "
                if x == self.width - 1:
                    end = "\n"
                actor = self.mapping[(x,y)].within
                if actor is None:
                    icon = ".  ."
                else:
                    icon = actor.icon
                print(f"{icon}", end=end)



class GridEntity:
    """
    Object which inhabits a Gridsquare.\n
    May be a static Location / Feature or dynamic Actor / Event.
    """

    def __init__(self, icon:str) -> None:
        self.icon = icon
        self.gmap:Gridmap = None
        self.gsquare:Gridsquare = None
    

    def toMap(self, gmap:Gridmap, coords:tuple=None) -> None:
        self.gmap = gmap
        if coords is not None:
            new_gsquare = gmap.mapping[coords]
        else:
            gsquare_full = True
            while gsquare_full:
                new_x = random.randint(0, (self.gmap.width - 1))
                new_y = random.randint(0, (self.gmap.height - 1))
                new_gsquare = self.gmap.mapping[(new_x, new_y)]
                if new_gsquare.within is None:
                    gsquare_full = False
        self.gsquare = new_gsquare
        self.gsquare.within = self



class AreaObstacle(GridEntity):
    """
    An obstacle on the areamap.
    Cannot move through or interact with.
    """



class PlayerGroup(GridEntity):
    """
    """

    def __init__(self, pc:PlayerCharacter, allies:list[Lifeform]=None, icon:str="Plyr") -> None:
        super().__init__(icon)
        self.pc = pc
        self.allies = allies



class NPCGroup(GridEntity):
    """
    Lifeform moving through a map.
    """

    def __init__(self, icon:str) -> None:
        super().__init__(icon)



class EnemyGroup(NPCGroup):
    """
    TODO:
    """

    LONE_MINDLESS = [[Mindless, "Mindless-1"]]
    LIGHT_MINDLESS = [[Mindless, "Mindless-1"], [Mindless, "Mindless-2"]]

    def __init__(self, group:list[list], icon:str="Hstl") -> None:
        super().__init__(icon)

        self.enemies = []
        for enemy in group:
            enemy_class = enemy[0]
            lifeform:Lifeform = enemy_class(enemy[1])
            if len(enemy) > 2:
                lifeform.equipWeapon(Weapon(enemy[2]))
            self.enemies.append(lifeform)


    def encounter(self, pg:PlayerGroup) -> bool:
        from encounters import Encounter
        encounter = Encounter(pg.pc, self.enemies, pg.allies)
        encounter.runEncounter()
        return True



class AreaLocationContext(metaclass=ABCMeta):
    """
    A Location to explore, visible on the Areamap.
    """

    areamap:object

    @abstractmethod
    def approach(self, pg:PlayerGroup) -> None:
        pass


    @abstractmethod
    def enter(self, pg:PlayerGroup) -> None:
        pass



class Cache(AreaLocationContext):
    """
    TODO:
    """

    @classmethod
    def approach(self, pg:PlayerGroup):
        reward = random.randint(1,13)
        pg.pc.gold_flakes += reward

        Interface.clear()
        print(f"Found {reward} gold flakes")
        Interface.pressEnter()



class PowerStation(AreaLocationContext):
    """
    TODO: docstring
    """

    @classmethod
    def approach(self, pg:PlayerGroup) -> bool:
        self.enter(pg)


    @classmethod
    def enter(self, pg:PlayerGroup) -> None:
        encounter = EncounterBuilder.build(pg.pc, "2", allies=pg.allies)
        encounter.runEncounter()



class HermeticJunction(AreaLocationContext):
    """
    TODO:
    """

    locked = True

    @classmethod
    def approach(self, pg:PlayerGroup):
        Interface.alert("The junctions")
        if self.locked:
            Interface.alert("im locked")
            self.locked = False
        else:
            Interface.alert("now im not")
            return True



class AreaLocation(GridEntity):
    """
    A container object which inhabits a Gridsquare's '.within' attribute.\n
    Contains an AreaLocationContext which defines what happens when func 'approach' is called.\n
    - 'icon' should be 4 char long (will eventually hold img file for display window)
    """

    invis_icon:str

    def __init__(self, icon:str, location:AreaLocationContext, hidden=False, replace=False) -> None:
        self.replace = replace
        self.hidden = hidden
        if hidden is True:
            self.invis_icon = icon
            icon = "????"
        super().__init__(icon)
        self.location = location
        self.hidden = hidden
        

    def approach(self, pg:PlayerGroup) -> None:
        if self.hidden is True:
            self.hidden = False
            self.icon = self.invis_icon
        subreplace = self.location.approach(pg)
        if subreplace is not None:
            self.replace = subreplace
        return self.replace



class AreaEvent(AreaLocation):
    """
    A dynamic type of AreaLocation.\n
    Defaults to hidden and replace on move.
    """

    def __init__(self, icon:str, location:AreaLocation, hidden=True, replace=True) -> None:
        super().__init__(icon, location, hidden, replace)



class AreaHub(AreaLocation):
    from hubs import Hub
    def __init__(self, icon:str, hub:Hub, hidden=False, replace=False) -> None:
        super().__init__(icon, hub, hidden, replace)



class Areamap:
    """
    TODO:
    """

    def __init__(self, context:type, title:str, gmap:Gridmap, pg:PlayerGroup) -> None:
        self.context = context
        self.title = title
        self.gmap = gmap
        self.pg = pg
        self.pc = pg.pc

    @abstractmethod
    def populate(self) -> None:
        pass

    
    def movePlayerGroup(self, pg:PlayerGroup, direction:tuple):
        cur_coords = pg.gsquare.coords
        new_coords = ((cur_coords[0] + direction[0]), (cur_coords[1] + direction[1]))
        if new_coords[0] < 0 or new_coords[0] > self.gmap.width - 1 or new_coords[1] < 0 or new_coords[1] > self.gmap.height - 1:
            return

        replace = False
        new_gsquare = self.gmap.mapping[new_coords]
        if isinstance(new_gsquare.within, AreaObstacle):
            pass
        elif isinstance(new_gsquare.within, EnemyGroup):
            replace = new_gsquare.within.encounter(self.pg)
        elif isinstance(new_gsquare.within, AreaEvent):
            replace = new_gsquare.within.approach(self.pg)
        elif isinstance(new_gsquare.within, AreaLocation):
            new_gsquare.within.location.areamap = self
            replace = new_gsquare.within.approach(self.pg)
            # if isinstance(new_gsquare.within, AreaHub):
            #     self.populate(self.gmap)
        else:
            replace = True

        if replace:
            self.pg.gsquare.within = None
            self.pg.gsquare = new_gsquare
            new_gsquare.within = self.pg


    def start(self, start_hub:AreaLocation=None) -> None:
        self.populate(self.gmap)
        if start_hub is not None:
            start_hub.location.approach(self.pg)

        isRunning = True
        while isRunning:
            Interface.clear()
            print(f"\t--- [ {self.title} ] ---\n")
            Interface.characterInfo(self.pc)
            self.gmap.display()
            user_input = input(f"\n\n[W] Up\n[A] Left\n[S] Down\n[D] Right\n\n[Enter] Wait\n[X] Quit\n\n").lower()
            if user_input in ["w", "a", "s", "d"]:
                direct_dict = {
                    "w": self.gmap.UP,
                    "a": self.gmap.LEFT,
                    "s": self.gmap.DOWN,
                    "d": self.gmap.RIGHT
                }
                direction = direct_dict[user_input]
                self.movePlayerGroup(self.pg, direction)
                if self.pc.hp < 1:
                    isRunning = False
            elif user_input == "x":
                raise QuitGame(self.pc)
                # isRunning = False