import random

import dimensions
from part_data import *

class Selector:
    PARTS = 4
    BRAIN,BODY,WEAPON,FOOT = range(4)
    def __init__(self, brains=BRAINS, bodies=BODIES, weapons=WEAPONS, feet=FEET):
        self.component_lists = [brains, bodies, weapons, feet]
        self.components = [0,0,0,0]
        
    def next(self, part):
        self.components[part] += 1
        self.components[part] = self.components[part] % len(self.component_lists[part])
                
    def prev(self, part):
        self.components[part] -= 1
        if self.components[part] == -1:
            self.components[part] += len(self.component_lists[part])
        
    def place(self, position=False):
        if not position:
            position = random.randint(0,dimensions.ARENA_W-1)
        
        return ("place " + str(position) + " " +
                self.component_lists[0][self.components[0]] + " " +
                self.component_lists[1][self.components[1]] + " " +
                self.component_lists[2][self.components[2]] + " " +
                self.component_lists[3][self.components[3]])

    def random_component(self):
        self.components = [random.randint(0,len(self.component_lists[x])-1) for x in range(4)]

    def body(self):
        return self.component_lists[1][self.components[1]]

    def weapon(self):
        return self.component_lists[2][self.components[2]]

    def brain(self):
        return self.component_lists[0][self.components[0]]

    def feet(self):
        return self.component_lists[3][self.components[3]]
