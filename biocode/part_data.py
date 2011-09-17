BRAINS =["alternate","empty","evaluate"]
BODIES =["porky","hardhead","hardsides"]
WEAPONS =["spikes","axes","ring"]
FEET =["straight","diagonal","knight"]

#feet
FORWARD = 0
DIAGONAL = 1
SIDE = 2

#brains
CHANGE = 0
NONE = 1
WAIT = 2

FEET_DATA = {"straight": [FORWARD],
             "diagonal": [DIAGONAL],
             "knight": [FORWARD, DIAGONAL]
             }

BODY_DATA = {"porky": (2, (False,False,False,False)),
             "hardhead": (1, (True, False, False, False)),
             "hardsides": (1, (False, False, True, True))}

BRAINS_DATA = {"alternate":[CHANGE],
               "empty": [NONE],
               "evaluate":[CHANGE, NONE, WAIT]}

WEAPON_DATA = {"spikes":(2,(True,False,False,False)),
               "axes":(2,(False,False,True,True)),
               "ring":(1,(True,True,True,True))}
