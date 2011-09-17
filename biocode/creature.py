import part_data
import dimensions

class Direction:
    UP, DOWN, LEFT, RIGHT = range(4)

BEHIND = {Direction.UP: Direction.DOWN,
          Direction.DOWN: Direction.UP,
          Direction.LEFT: Direction.RIGHT,
          Direction.RIGHT: Direction.LEFT}

LEFT = {Direction.UP: Direction.LEFT,
          Direction.DOWN: Direction.RIGHT,
          Direction.LEFT: Direction.DOWN,
          Direction.RIGHT: Direction.UP}

RIGHT = {Direction.UP: Direction.RIGHT,
          Direction.DOWN: Direction.LEFT,
          Direction.LEFT: Direction.UP,
          Direction.RIGHT: Direction.DOWN}

    
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

    def forward(self,arena_map):
        try_x, try_y = self.pos_x, self.pos_y
        if self.direction == Direction.UP:
            try_y -= 1
        elif self.direction == Direction.DOWN:
            try_y += 1
        if self.direction == Direction.LEFT:
            try_x -= 1
        elif self.direction == Direction.RIGHT:
            try_x += 1

        try:
            if not arena_map[try_x][try_y]:
                self.pos_x, self.pos_y = try_x, try_y
        except IndexError:
            self.pos_x, self.pos_y = try_x, try_y
                
    def side(self,arena_map):
        if self.pos_x == 0 or self.pos_x == dimensions.ARENA_W-1:
            self.r_or_l = -self.r_or_l

        try_x, try_y = self.pos_x, self.pos_y
            
        if self.direction == Direction.UP:
            try_x -= self.r_or_l
        elif self.direction == Direction.DOWN:
            try_x += self.r_or_l
        if self.direction == Direction.LEFT:
            try_y -= self.r_or_l
        elif self.direction == Direction.RIGHT:
            try_y += self.r_or_l

        try:
            if not arena_map[try_x][try_y]:
                self.pos_x, self.pos_y = try_x, try_y
        except IndexError:
            pass

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

        self.health, self.shields = part_data.BODY_DATA[self.body]

        self.brain_list = part_data.BRAINS_DATA[self.brain]
        self.brain_counter = 0

        self.damage, self.threat_area = part_data.WEAPON_DATA[self.weapon]
        
    def update(self, arena_map):
        self.brain_counter += 1
        self.brain_counter = self.brain_counter%len(self.brain_list)
        if self.brain_list[self.brain_counter] == part_data.CHANGE:
            self.r_or_l = -self.r_or_l
        elif self.brain_list[self.brain_counter] == part_data.NONE:
            pass
        elif self.brain_list[self.brain_counter] == part_data.WAIT:
            return

        self.move_counter += 1
        self.move_counter = self.move_counter%len(self.move_list)
        if self.move_list[self.move_counter] == part_data.FORWARD:
            self.forward(arena_map)
        elif self.move_list[self.move_counter] == part_data.DIAGONAL:
            self.forward(arena_map)
            self.side(arena_map)
