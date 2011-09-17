'''
* This file is part of Biocode.
* Copyright (c) Hans Lo
*
* Touhou SRPG is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* Touhou SRPG is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with Touhou SRPG.  If not, see <http://www.gnu.org/licenses/>.
'''

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
