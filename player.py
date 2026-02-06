import pygame
from settings import GRAVITY, JUMP_FORCE, GREEN

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40,40)
        self.vel_y = 0
        self.on_ground = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)