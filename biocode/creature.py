class Direction:
    UP, DOWN, LEFT, RIGHT = range(4)

class Creature:
    
    def __init__(self, player_number, direction):
        self.pos_x = None
        self.pos_y = None
        self.damage = 1
        self.player = player_number
        self.direction = direction
        
    def update(self):
        pass

    def set_pos(self, pos):
        self.pos_x, self.pos_y = pos

    def forward(self):
        if self.direction == Direction.UP:
            self.pos_y -= 1
        elif self.direction == Direction.DOWN:
            self.pos_y += 1
        if self.direction == Direction.LEFT:
            self.pos_x -= 1
        elif self.direction == Direction.RIGHT:
            self.pos_x += 1

class NoobSauce(Creature):

    def __init__(self, player_number, direction):
        Creature.__init__(self, player_number, direction)

    def update(self):
        self.forward()
    
