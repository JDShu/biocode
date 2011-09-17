import ui
import creature
import base

STARTING_DIRECTION = {base.BOTTOM: creature.Direction.UP,
                      base.TOP: creature.Direction.DOWN,
                      base.LEFT: creature.Direction.RIGHT,
                      base.RIGHT: creature.Direction.LEFT}

class Type:
    HUMAN = 0
    AI = 1
    TEST = 2
    
class Player:

    def __init__(self, player_number, health=10):
        self.health = 10
        self.player_number = player_number
        self.action = None
        self.base = None
        
    def act(self, arena):
        if self.action:
            command = self.action.split()
            print command
            if command[0] == "place":
                try:
                    i = int(command[1])
                    if self.base == base.TOP:
                        place = (i,0)
                    elif self.base == base.BOTTOM:
                        place = (i,arena.l-1)
                    arena.add_creature(creature.NoobSauce(self.player_number,STARTING_DIRECTION[self.base]),place)
                except ValueError:
                    print "invalid command"

class Human(Player):
    
    def __init__(self, player_number, health=10):
        Player.__init__(self,player_number, health)
        self.scanner = ui.Scanner()
        
    def scan_input(self):
        self.action = self.scanner.scan()
        if self.action:
            print self.action

class AI(Player):
    def __init__(self, player_number, health=10):
        Player.__init__(self,player_number, health)
        
    def scan_input(self):
        pass
        
class Test(Player):
    def __init__(self, player_number, health=10):
        Player.__init__(self,player_number, health)        
        self.command = None
        self.repeat = 0

    def set_command(self, command, repeat=1):
        self.command = command
        print "command set to", command
        self.repeat = repeat
        
    def scan_input(self):
        if self.repeat > 0:
            print self.action
            self.action = self.command
            self.repeat -= 1
        else:
            self.action = None
        
