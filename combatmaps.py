from gridmaps import Gridsquare, Gridmap
from areas import PlayerGroup


class CombatmapActor:
    """
    """

    def __init__(self, gmap:Gridmap, gsquare:Gridsquare, icon:str) -> None:
        self.icon = icon
        self.gmap = gmap
        self.gsquare = gsquare
    


class Combatmap:
    """
    """

    def __init__(self, gmap:Gridmap, pg:PlayerGroup) -> None:
        self.gmap = gmap
        self.pg = pg



class CombatmapBuilder:
    """
    """

    @classmethod
    def build(self, width:int, height:int) -> Combatmap:
        gmap = Gridmap(width, height)
        