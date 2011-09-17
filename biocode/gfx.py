import pygame
import os

class Drawer:
    
    CREATURE = pygame.image.load(os.path.join("biocode","creature.png"))

    def __init__(self,arena,dim=(400,400)):
        self.w, self.h = dim
        self.cell_w = self.w/arena.w
        self.cell_h = self.h/arena.l
        self.panel_w, self.panel_h = (200,self.h)
        pygame.init()
        self.screen = pygame.display.set_mode((self.w + self.panel_w,self.panel_h))
        pygame.display.set_caption("Biocode")

        self.CREATURE = pygame.transform.scale(self.CREATURE, (self.cell_w, self.cell_h))
        
    def draw_arena(self, arena):
        self.screen.fill((0,0,0))

        #panel ui
        
        
        #arena
        for x, row in enumerate(arena.map):
            for y, space in enumerate(row):
                if space:
                    self.screen.blit(self.CREATURE,(self.panel_w + x*self.cell_w, y*self.cell_h))
        pygame.display.flip()

    def draw_panel(self, panel):
        pass
