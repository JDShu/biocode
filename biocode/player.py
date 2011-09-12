import ui
import creature

class Player:

    def __init__(self, player_number, health=10):
        self.health = 10
        self.player_number = player_number
        self.action = None
        
    def act(self, arena):
        if self.action:
            command = self.action.split()
            print command
            if command[0] == "place":
                try:
                    x = int(command[1])
                    if 0 <= x < 10:
                        arena.add_creature(creature.NoobSauce(),(x,0))
                except ValueError:
                    print "invalid command"

class Human(Player):
    
    def __init__(self, player_number, health=10):
        Player.__init__(self,player_number, health)
        self.scanner = ui.Scanner()
        self.action = None
        
    def scan_input(self):
        self.action = self.scanner.scan()
        if self.action:
            print self.action

    def act(self, arena):
        if self.action:
            command = self.action.split()
            print command
            if command[0] == "place":
                try:
                    x = int(command[1])
                    if 0 <= x < 10:
                        arena.add_creature(creature.NoobSauce(),(x,0))
                except ValueError:
                    print "invalid command"    
                    
class AI(Player):
    pass
