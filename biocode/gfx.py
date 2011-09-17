import pygame
import os

from dimensions import CELL_W, CELL_H

class Drawer:
    
    CREATURE = pygame.image.load(os.path.join("biocode","creature.png"))
    LEFT_BUTTON = pygame.image.load(os.path.join("biocode","left_button.png"))
    RIGHT_BUTTON = pygame.image.load(os.path.join("biocode","right_button.png"))
    
    def __init__(self,arena):
        self.w, self.h = CELL_W*arena.w, CELL_H*arena.l
        self.panel_w, self.panel_h = (200,self.h)
        pygame.init()
        self.screen = pygame.display.set_mode((self.w + self.panel_w,self.panel_h))
        pygame.display.set_caption("Biocode")

        self.CREATURE = pygame.transform.scale(self.CREATURE, (CELL_W, CELL_H))
        self.LEFT_BUTTON = pygame.transform.scale(self.LEFT_BUTTON, (CELL_W,CELL_H))
        self.RIGHT_BUTTON = pygame.transform.scale(self.RIGHT_BUTTON, (CELL_W,CELL_H))
    def draw(self, arena, panel):
        self.draw_arena(arena)
        self.draw_panel(panel)
        pygame.display.flip()
        
    def draw_arena(self, arena):
        self.screen.fill((0,0,0))

        for x, row in enumerate(arena.map):
            for y, space in enumerate(row):
                if space:
                    self.screen.blit(self.CREATURE,(self.panel_w + x*CELL_W, y*CELL_H))

    def draw_panel(self, panel):
        if not panel:
            return
        for region in panel.click_regions:
            if region.action == panel.selector.next:
                self.screen.blit(self.LEFT_BUTTON, (region.x, region.y))
            elif region.action == panel.selector.prev:
                self.screen.blit(self.RIGHT_BUTTON, (region.x, region.y))
