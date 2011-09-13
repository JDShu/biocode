class Creature:
    
    def __init__(self, player_number):
        self.pos_x = None
        self.pos_y = None
        self.damage = 1
        self.player = player_number
        
    def update(self):
        pass

    def set_pos(self, pos):
        self.pos_x, self.pos_y = pos
    
class NoobSauce(Creature):

    def __init__(self, player_number):
        Creature.__init__(self, player_number)

    def update(self):
        Creature.update(self)
        self.pos_y += 1
    
