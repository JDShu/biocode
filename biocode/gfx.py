import pygame
import os

from dimensions import CELL_W, CELL_H
import part_data

class Drawer:
    pygame.init()
    FONT = pygame.font.Font(None,20)
    BODIES = {}
    for b in part_data.BODIES:
        BODIES[b] = pygame.image.load(os.path.join("biocode",b +".png"))
        BODIES[b] = pygame.transform.scale(BODIES[b], (CELL_W,CELL_H))
        BODIES[b] = (pygame.transform.rotate(BODIES[b], 90), pygame.transform.rotate(BODIES[b], 270))
        
    WEAPONS = {}
    for w in part_data.WEAPONS:
        WEAPONS[w] = pygame.image.load(os.path.join("biocode",w +".png"))
        WEAPONS[w] = pygame.transform.scale(WEAPONS[w], (CELL_W,CELL_H))
        WEAPONS[w] = (pygame.transform.rotate(WEAPONS[w], 90), pygame.transform.rotate(WEAPONS[w], 270))
        
    LEFT_BUTTON = pygame.image.load(os.path.join("biocode","left_button.png"))
    RIGHT_BUTTON = pygame.image.load(os.path.join("biocode","right_button.png"))
    
    def __init__(self,arena):
        self.w, self.h = CELL_W*arena.w, CELL_H*arena.l
        self.panel_w, self.panel_h = (200,self.h)
        
        self.screen = pygame.display.set_mode((self.w + self.panel_w,self.panel_h))
        pygame.display.set_caption("Biocode")

        self.LEFT_BUTTON = pygame.transform.scale(self.LEFT_BUTTON, (CELL_W,CELL_H))
        self.RIGHT_BUTTON = pygame.transform.scale(self.RIGHT_BUTTON, (CELL_W,CELL_H))
    def draw(self, arena, panel,player_1,player_2):
        self.draw_arena(arena)
        self.draw_panel(panel)
        self.draw_player(player_1)
        self.draw_player(player_2)
        pygame.display.flip()
        
    def draw_arena(self, arena):
        self.screen.fill((255,255,255))

        for x, row in enumerate(arena.map):
            for y, creature in enumerate(row):
                if creature:
                    self.screen.blit(self.BODIES[creature.body][creature.player-1],(self.panel_w + x*CELL_W, y*CELL_H)) #hack player number
                    self.screen.blit(self.WEAPONS[creature.weapon][creature.player-1],(self.panel_w + x*CELL_W, y*CELL_H))

    def draw_panel(self, panel):
        if not panel:
            return
        for region in panel.click_regions:
            if region.action == panel.selector.next:
                self.screen.blit(self.LEFT_BUTTON, (region.x, region.y))
            elif region.action == panel.selector.prev:
                self.screen.blit(self.RIGHT_BUTTON, (region.x, region.y))
        self.screen.blit(self.BODIES[panel.selector.body()][0],(20, 300)) #hack player number
        self.screen.blit(self.WEAPONS[panel.selector.weapon()][0],(20, 300))

        brain_text = self.FONT.render("Brain: " + panel.selector.brain(), False, (0,0,0))
        body_text = self.FONT.render("Body: " + panel.selector.body(), False, (0,0,0))
        weapon_text = self.FONT.render("Weapon: " + panel.selector.weapon(), False, (0,0,0))
        feet_text = self.FONT.render("Feet: " + panel.selector.feet(), False, (0,0,0))
        
        self.screen.blit(brain_text,(20,350))
        self.screen.blit(body_text,(20,365))
        self.screen.blit(weapon_text,(20,380))
        self.screen.blit(feet_text,(20,395))
        
    def draw_player(self, player):
        s = self.FONT.render("Player " + str(player.player_number) + ": " + str(player.health), False, (255,0,0))
        self.screen.blit(s,(20,400 + player.player_number*20))
