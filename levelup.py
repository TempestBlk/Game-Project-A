class Levelup():
    level_list = {
        1: 0,
        2: 10,
        3: 25,
        4: 40,
        5: 65,
        6: 90,
        7: 130,
        8: 180,
        9: 250,
        10: 350
    }


    @classmethod
    def check(self, lifeform):
        from interface import Interface
        from lifeforms import Lifeform
        checking = True
        while checking:
            if lifeform.xp >= Levelup.level_list[(lifeform.level + 1)]:
                lifeform.level += 1

                lifeform.max_hp += 2
                lifeform.hp += 2
                
                lifeform.xp -= Levelup.level_list[(lifeform.level)]
                Interface.levelupMessage(lifeform)
            else:
                checking = False