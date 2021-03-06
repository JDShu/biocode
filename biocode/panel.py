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

import selector
from dimensions import CELL_W, CELL_H

SPACING = 60

class Panel:

    def __init__(self,dim, arena):
        self.w, self.h = dim
        self.selector = selector.Selector()
        self.switcher_pos = (10,10)
        self.health = None
        self.click_regions = [ClickRegion((10, 10 + x*SPACING, 50, 50), self.selector.next, x) for x in range(self.selector.PARTS)]
        self.click_regions += [ClickRegion((60, 10 + x*SPACING, 50, 50), self.selector.prev, x) for x in range(self.selector.PARTS)]
        self.click_regions += [ClickRegion((self.w+CELL_W*x, (arena.l-1)*CELL_H,CELL_W, CELL_H), self.selector.place, x) for x in range(arena.w)]
    
    def scan(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for r in self.click_regions:
                    result = r.execute(pos)
                    if result:
                        return result
class ClickRegion:

    def __init__(self, dim, action, arg):
        self.x, self.y, self.w, self.h = dim
        self.arg = arg
        self.action = action
        
    def execute(self, pos):
        if (self.x < pos[0] < (self.x + self.w) and
            self.y < pos[1] < (self.y + self.h)):
            return self.action(self.arg)
        return None
