import base
import dimensions
from creature import BEHIND, LEFT, RIGHT, Direction

class Arena:

    def __init__(self):
        self.w, self.l = dimensions.ARENA_W, dimensions.ARENA_L
        self.map = [[None]*self.w for i in xrange(self.l)]
        self.creatures = []
        self.turn_results = []
        
    def update(self):
        for c in self.creatures:
            self.place_creature(None, (c.pos_x,c.pos_y))
            c.update(self.map)
            if c.pos_x == 0:
                self.turn_results += [Result(Result.EXIT_LEFT, c)]
                self.creatures.remove(c)
            elif c.pos_x > self.w-1:
                self.turn_results += [Result(Result.EXIT_RIGHT, c)]
                self.creatures.remove(c)
            elif c.pos_y < 0:
                self.turn_results += [Result(Result.EXIT_TOP, c)]
                self.creatures.remove(c)
            elif c.pos_y > self.l-1:
                self.turn_results += [Result(Result.EXIT_BOTTOM, c)]
                self.creatures.remove(c)
            else:
                self.place_creature(c, (c.pos_x,c.pos_y))
        self.combat()
                
    def combat(self):
        #determine threat spaces list (coords and direction for each)
        threat_spaces = []
        for c in self.creatures:
            if c.threat_area[0]:
                threat_spaces += [(c.pos_x,c.pos_y,c.direction,c.damage)]
            elif c.threat_area[1]:
                threat_spaces += [(c.pos_x,c.pos_y,BEHIND[c.direction],c.damage)]
            elif c.threat_area[2]:
                threat_spaces += [(c.pos_x,c.pos_y,LEFT[c.direction],c.damage)]
            elif c.threat_area[3]:
                threat_spaces += [(c.pos_x,c.pos_y,RIGHT[c.direction],c.damage)]

        for t in threat_spaces:
            try:
                if t[2] == Direction.UP:
                    if self.map[t[0]][t[1]-1]:
                        self.process_damage(self.map[t[0]][t[1]-1],c.damage)
                    elif t[2] == Direction.DOWN:
                        if self.map[t[0]][t[1]+1]:
                            self.process_damage(self.map[t[0]][t[1]+1],c.damage)
                    elif t[2] == Direction.LEFT:
                        if self.map[t[0]-1][t[1]]:
                            self.process_damage(self.map[t[0]-1][t[1]],c.damage)
                    elif t[2] == Direction.RIGHT:
                        if self.map[t[0]+1][t[1]]:
                            self.process_damage(self.map[t[0]+1][t[1]],c.damage)
            except IndexError:
                pass
                            
    def process_damage(self, creature, damage):
        creature.health -= damage
        if creature.health <= 0:
            self.creatures.remove(creature)
            self.place_creature(None, (creature.pos_x, creature.pos_y))
            
    def add_creature(self, creature, pos):
        creature.set_pos(pos)
        self.creatures.append(creature)
        self.place_creature(creature, pos)
                
    def place_creature(self, creature, pos):
        self.map[pos[0]][pos[1]] = creature

    def execute_results(self, *players):
        for r in self.turn_results:
            if r.result_type == Result.EXIT_LEFT:
                damage(players, base.LEFT, r.argument.damage)
            elif r.result_type == Result.EXIT_RIGHT:
                damage(players, base.RIGHT, r.argument.damage)
            elif r.result_type == Result.EXIT_TOP:
                damage(players, base.TOP, r.argument.damage)
            elif r.result_type == Result.EXIT_BOTTOM:
                damage(players, base.BOTTOM, r.argument.damage)
       
        self.turn_results = []

class Result:
    
    EXIT_TOP, EXIT_BOTTOM, EXIT_LEFT, EXIT_RIGHT = range(4)

    def __init__(self, result_type, argument):
        self.result_type = result_type
        self.argument = argument
    
def damage(players, player_base, damage):
    for p in players:
        if p.base == player_base:
            p.health -= damage
