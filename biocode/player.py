'''
* This file is part of Biocode.
* Copyright (c) Hans Lo
*
* Touhou SRPG is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* Touhou SRPG is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with Touhou SRPG.  If not, see <http://www.gnu.org/licenses/>.
'''

import ui
import creature
import base
import panel
import selector

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
            if command[0] == "place":
                try:
                    i = int(command[1])
                    if self.base == base.TOP:
                        place = (i,0)
                    elif self.base == base.BOTTOM:
                        place = (i,arena.l-1)
                    components = [command[i] for i in range(2,6)]
                    arena.add_creature(creature.CustomCreature(self.player_number,STARTING_DIRECTION[self.base], components), place)
                except ValueError:
                    print "invalid command"
            self.action = None

    def do_turn(self):
        pass
                    
class Human(Player):
    
    def __init__(self, player_number, arena, health=10):
        Player.__init__(self,player_number, health)
        self.scanner = ui.Scanner(panel.Panel((200,400),arena)) #magic number
        
    def scan_input(self):
        self.action = self.scanner.scan()
        
class AI(Player):
    def __init__(self, player_number, arena, health=10, period=2, creature_per_turn=1):
        Player.__init__(self,player_number, health)
        self.period = period
        self.count = period
        self.selector = selector.Selector()
        
    def scan_input(self):
        if self.count == 0:
            self.count = self.period
            self.selector.random_component()
            self.action = self.selector.place()

    def do_turn(self):
        self.count -= 1
        self.action = None
        
class Test(Player):
    def __init__(self, player_number, arena, health=10):
        Player.__init__(self,player_number, health)
        self.command = None
        self.repeat = 0

    def set_command(self, command, repeat=1):
        self.command = command
        self.repeat = repeat
        
    def scan_input(self):
        if self.repeat > 0:
            self.action = self.command
            self.repeat -= 1
        else:
            self.action = None
        
