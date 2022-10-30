from interface import Interface



class Levelup():
    level_list = {
        1: 0,
        2: 10,
        3: 25,
        4: 40,
        5: 65
    }


    def check(lifeform):
        checking = True
        while checking:
            if lifeform.xp >= Levelup.level_list[(lifeform.level + 1)]:
                lifeform.level += 1
                lifeform.xp -= Levelup.level_list[(lifeform.level)]
                Interface.levelupMessage(lifeform)
            else:
                checking = False