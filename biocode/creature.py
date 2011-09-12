class Creature:
    
    def __init__(self):
        self.pos_x = None
        self.pos_y = None
        self.damage = 1
        
    def update(self):
        pass

    def set_pos(self, pos):
        self.pos_x, self.pos_y = pos
    
class NoobSauce(Creature):

    def __init__(self):
        Creature.__init__(self)

    def update(self):
        Creature.update(self)
        self.pos_y += 1
    
