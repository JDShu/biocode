import string
import pygame
from pygame.locals import *

class Scanner:

    def __init__(self):
        print "init"
        self.command = []
        self.player_action = None
        
    def scan(self):
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

        action = self.player_action
        self.player_action = None
        return action
