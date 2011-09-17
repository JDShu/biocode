BRAINS =["brain1","brain2","brain3"]
BODIES =["body1","body2","body3"]
WEAPONS =["weapon1","weapon2","weapon3"]
FEET =["feet1","feet2","feet3"]


class Selector:
    PARTS = 4
    BRAIN,BODY,WEAPON,FOOT = range(4)
    def __init__(self, brains=BRAINS, bodies=BODIES, weapons=WEAPONS, feet=FEET):
        self.component_lists = [brains, bodies, weapons, feet]
        self.components = [0,0,0,0]
        
    def next(self, part):
        self.components[part] += 1
        self.components[part] = self.components[part] % len(self.component_lists[part])
        print "selected", self.component_lists[part][self.components[part]]
        
    def prev(self, part):
        self.components[part] -= 1
        if self.components[part] == -1:
            self.components[part] += len(self.component_lists[part])
        print "selected", self.component_lists[part][self.components[part]]

    def place(self, position):
        print "create at", position
        return "place " + str(position)
        
    def return_creature(self):
        return ComponentCollection(*[self.component_lists[self.components[x]]
                                     for x in range(PARTS)])

class ComponentCollection:
    def __init__(self, brain, body, weapon, feet):
        self.brain = brain
        self.body = body
        self.weapon = weapon
        self.feet = feet
        print "new creature:", brain, body, weapon, feet
