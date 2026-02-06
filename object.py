import pygame
from settings import GRAY, RED

class Block:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)

class Spike: 
    def __init__(self , x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
    
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)