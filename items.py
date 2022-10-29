from attacks import Attack



class Weapons():
    metal_pipe = {
        "id": "metal_pipe",
        "name": "Metal Pipe",
        "durability": 50,
        "basePrice": 4,
        "attacks": [Attack.metal_pipe_slam, Attack.metal_pipe_swing]
        }

    shiv = {
        "id": "shiv",
        "name": "Shiv",
        "durability": 30,
        "basePrice": 2,
        "attacks": [Attack.shiv_stab]
    }   
        


class Wearables():
    # protection for parts --> [slash, pierce, blunt]
    # onEquip add protection scores to lifeform stats, 

    junior_researcher_coat = {
        "id": "junior_researcher_coat",
        "name": "Junior Researcher Coat",
        "durability": 250,
        "basePrice": 160,
        "protection": {
            "torso": [4,1,1],
            "stomach": [1,1,1],
            "arms": [2,1,1],
        }
    }



class Item():
    def __init__(self):
        pass



class Weapon(Item):
    def __init__(self, weapon):
        self.id = weapon['id']
        self.name = weapon['name']
        self.durability = weapon['durability']
        self.basePrice = weapon['basePrice']
        self.attacks = weapon['attacks']



class Wearable(Item):
    def __init__(self, wearable):
        self.id = wearable['id']
        self.name = wearable['name']
        self.durability = wearable['durability']
        self.basePrice = wearable['basePrice']
        self.protection = wearable['protection']