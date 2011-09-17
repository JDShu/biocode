class Selector:
    BRAIN,BODY,WEAPON,FOOT = range(4)
    def __init__(self, brains, bodies, weapons, feet):
        self.component_lists = [brains, bodies, weapons, feet]
        self.components = [0,0,0,0]

    def next(self, part):
        self.components[part] += 1
        self.components[part] = self.components[part] % len(self.component_lists[part])

    def prev(self, part):
        self.components[part] -= 1
        if self.components[part] == -1:
            self.components[part] += len(self.component_lists[part])
        
    def return_creature(self):
        return ComponentCollection(self.brains[self.components[self.BRAIN]],
                                   self.bodies[self.components[self.BODY]],
                                   self.weapons[self.components[self.WEAPON]],
                                   self.feet[self.components[self.FOOT]])

class ComponentCollection:
    def __init__(self, brain, body, weapon, feet):
        self.brain = brain
        self.body = body
        self.weapon = weapon
        self.feet = feet
