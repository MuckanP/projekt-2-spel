import pygame
from settings import GRAVITY, JUMP_FORCE, GREEN

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40,40)
        self.vel_y = 0
        self.on_ground = False
        
    def update(self, blocks):
        self.rect = GRAVITY
        self.vel_y = self.vel_y
        self.on_ground = False
        
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.vel_y > 0:
                    self.rect.bottom = block.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    
    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_FORCE

    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)
        
        