import pygame
from settings import GRAY, RED, TILE_SIZE

class Block:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, self.rect)

class Spike: 
    def __init__(self , x, y, w, h):
        self.rect = pygame.Rect(x + (TILE_SIZE - w) // 2, y + (TILE_SIZE - h) // 2, w, h)
                                #detta gör spiken triangulär och centrerad i tile
        self.x = x  # spara original position
        self.y = y
        
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
    
    def draw(self, screen):
        points = [
            (self.rect.centerx, self.rect.top),  # topp av triangeln
            (self.rect.left, self.rect.bottom),   # vänsterbottten
            (self.rect.right, self.rect.bottom)   # högerbotten
        ]
        pygame.draw.polygon(screen, RED, self.rect)