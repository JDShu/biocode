import pygame
import os

class Drawer:
    
    CREATURE = pygame.image.load(os.path.join("biocode","creature.png"))

    def __init__(self,arena,dim=(400,400)):
        self.w, self.h = dim
        self.cell_w = self.w/arena.w
        self.cell_h = self.h/arena.l
        pygame.init()
        self.screen = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption("Biocode")

        self.CREATURE = pygame.transform.scale(self.CREATURE, (self.cell_w, self.cell_h))
        
    def draw(self, arena):
        self.screen.fill((0,0,0))
        for x, row in enumerate(arena.map):
            for y, space in enumerate(row):
                if space:
                    self.screen.blit(self.CREATURE,(x*self.cell_w, y*self.cell_h))
        
        pygame.display.flip()

