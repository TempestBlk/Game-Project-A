class Levels():
    lvl_dict = {
        1:0, 2:100, 3:250, 4:450, 5:750, 6:1250, 7:2150, 8:3350
    }
    
    def check_lvlup(entity, lvl_dict=lvl_dict):
        lvl = entity.get_lvl()
        exp = entity.get_exp()
        lvlup_req = lvl_dict[lvl + 1] # NOTE: does not support multiple levelups in a signle check
        if exp >= lvlup_req:
            entity.add_lvl()
            entity.set_exp(lvlup_req - exp)