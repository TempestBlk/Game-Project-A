
from gridmaps import Gridmap, Areamap, PlayerGroup, EnemyGroup, AreaLocation, AreaObstacle, AreaEvent, AreaHub, Cache, PowerStation, HermeticJunction
from hubs import NorthWingSZ


class LabC1NorthWing(Areamap):
    """
    New game area.\n\n
    The Secure Zone (hub) is in the southwest sector.\n
    Mindless roaming lab C1 threaten anyone who ventures beyond the Hermetic Junction.
    """

    @staticmethod
    def populate(gmap:Gridmap):
        for _ in range(4):
            eg = EnemyGroup(EnemyGroup.LONE_MINDLESS, icon="1 Lf")
            eg.toMap(gmap)

        for _ in range(1):
            eg = EnemyGroup(EnemyGroup.LIGHT_MINDLESS, icon="2 Lf")
            eg.toMap(gmap)

        for _ in range(3):
            o = AreaObstacle(icon="~#+~")
            o.toMap(gmap)

        for _ in range(3):
            c = AreaEvent(icon="Signal", location=Cache)
            c.toMap(gmap)
    
    
    @classmethod
    def build(self, pc):
        gmap = Gridmap(width=15, height=15)

        north_wing_sz = AreaHub(icon="NWSZ", hub=NorthWingSZ)
        north_wing_sz.toMap(gmap, (5,13))

        player_group = PlayerGroup(pc)
        player_group.toMap(gmap, (6,13))

        power_station = AreaLocation(icon="PwrS", location=PowerStation, hidden=True)
        power_station.toMap(gmap, (12,1))

        coords = 9,14
        for _ in range(11):
            ns_wall = AreaObstacle(icon=" || ")
            ns_wall.toMap(gmap, (coords))
            coords = coords[0], (coords[1] - 1)
        
        coords = 0,4
        for _ in range(9):
            ew_wall = AreaObstacle(icon="====")
            ew_wall.toMap(gmap, (coords))
            coords = coords[0] + 1, (coords[1])

        cn_wall = AreaObstacle(icon="=== ")
        cn_wall.toMap(gmap, (9,4))

        coords = (4,14)
        for _ in range(5):
            ns_wall = AreaObstacle(icon=" || ")
            ns_wall.toMap(gmap, (coords))
            coords = coords[0], (coords[1] - 1)

        coords = (3,9)
        for _ in range(3):
            ew_wall = AreaObstacle(icon="====")
            ew_wall.toMap(gmap, (coords))
            coords = coords[0] + 1, (coords[1])

        herm_junc = AreaLocation(icon="Junc", location=HermeticJunction, hidden=True)
        herm_junc.toMap(gmap, (1,4))

        # for _ in range(2):
        #     o = AreaObstacle(icon="~+##+~")
        #     o.toMap(gmap)

        areamap = self(self, "Lab C1 - North Wing", gmap, player_group)
        areamap.start(start_hub=north_wing_sz)