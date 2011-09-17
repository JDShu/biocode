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

import string
import pygame

from pygame.locals import *

import panel

class Scanner:

    def __init__(self, panel=None):
        self.command = []
        self.player_action = None
        self.panel = panel
        
    def scan(self):
        if self.panel == None:
            for e in pygame.event.get(KEYDOWN):
                if e.key == K_RETURN:
                    self.player_action = string.join(self.command,"")
                    self.command = []
                elif e.key == K_BACKSPACE:
                    self.command = self.command[:-1]
                elif K_a <= e.key <= K_z or K_0 <= e.key <= K_9 or e.key == K_SPACE:
                    self.command.append(chr(e.key))
                else:
                    self.player_action = None

            for e in pygame.event.get(MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
                            
        else:
            self.player_action = self.panel.scan()
        
        action = self.player_action
        self.player_action = None
        return action
