import part_data
import dimensions

class Direction:
    UP, DOWN, LEFT, RIGHT = range(4)

class Creature:
    
    def __init__(self, player_number, direction):
        self.pos_x = None
        self.pos_y = None
        self.damage = 1
        self.player = player_number
        self.direction = direction
        self.r_or_l = 1
        
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

    def side(self):
        if self.pos_x == 0 or self.pos_x == dimensions.ARENA_W-1:
            self.r_or_l = -self.r_or_l
        
        if self.direction == Direction.UP:
            self.pos_x -= self.r_or_l
        elif self.direction == Direction.DOWN:
            self.pos_x += self.r_or_l
        if self.direction == Direction.LEFT:
            self.pos_y -= self.r_or_l
        elif self.direction == Direction.RIGHT:
            self.pos_y += self.r_or_l
            
        
class NoobSauce(Creature):

    def __init__(self, player_number, direction):
        Creature.__init__(self, player_number, direction)

    def update(self):
        self.forward()
    
class CustomCreature(Creature):
    def __init__(self, player_number, direction, components):
        self.brain = components[0]
        self.body = components[1]
        self.weapon = components[2]
        self.feet = components[3]
        Creature.__init__(self, player_number, direction)

        self.move_list = part_data.FEET_DATA[self.feet]
        self.move_counter = 0
        
    def update(self):
        if self.move_list[self.move_counter] == part_data.FORWARD:
            self.forward()
        elif self.move_list[self.move_counter] == part_data.DIAGONAL:
            self.forward()
            self.side()
        self.move_counter += 1
        self.move_counter = self.move_counter%len(self.move_list)
