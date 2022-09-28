class Attacks():
    atk_dict = {
        "Slam":{
            'name': 'Slam',
            'hitMod': 0,
            'dmgRoll': [3, 4, 1],
            'dmgType': 'blugeoning'
            },
        "Fists":{
            'name': 'Fists',
            'hitMod': 0,
            'dmgRoll': [2, 4, 1],
            'dmgType': 'blugeoning'
            },
        "Annihilate":{
            'name': 'Annihilate',
            # NOTE: 'flavorText': ["_attacker is still for a moment then gestures toward _target"],
            'hitMod': 10,
            'dmgRoll': [5, 20, 20],
            'dmgType': 'quantum'
            }
    }