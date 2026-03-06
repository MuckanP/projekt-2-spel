import pygame
from settings import *
from player import Player
from level import Level


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game_state = "menu"

player = Player(100, HEIGHT - 80)
level = Level("levels/level1.txt")

attempts = 1

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    player.update(level.blocks)
    level.update(SCROLL_SPEED)
    
    # if game_state == "menu": # meny finns inte än så länge
    #     menu.draw(screen) # kommer bygga en meny på detta
        
    if game_state == "game": # byt till elif när övre raden funkar
        player.update(level.blocks)
        level.update(SCROLL_SPEED)
        
        for spike in level.spikes: # för spike collisions 
            if player.rect.colliderect(spike.rect):
                attempts + 1
                print("Attempt " attempts)
        
        screen.fill(WHITE)
        level.draw(screen)
        player.draw(screen)
    
    pygame.display.flip()