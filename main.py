import sys
import pygame
from settings import *
from player import Player
from level import Level

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game_state = "game"  # ändra till menu när menu funkar

player = Player(100, Height - 80)  # fixade y-positionen
level = Level("level1.txt")  # lägg till en level1.txt i samma mapp som main.py, eller ändra sökvägen här

attempts = 1

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if game_state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # flyttad in i keydown check
                    pygame.quit()
                    sys.exit()
                game_state = "game"
                
        elif game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
    
    if game_state == "game": 
        player.update(level.blocks)
        level.update(SCROLL_SPEED)
        
        for spike in level.spikes:  # för spike collisions 
            if player.rect.colliderect(spike.rect):
                attempts += 1  # var attempt + 1 innan, uppdaterade inte variabeln tydligen
                print("Attempt ", attempts)
                player.rect.x = 100
                player.rect.y = Height - 80
                player.vel_y = 0
                    # en reset av spelaren, bara där för säkerhets skull
                    
        screen.fill(WHITE)
        level.draw(screen)
        player.draw(screen)
    
    pygame.display.flip()