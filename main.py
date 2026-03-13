import sys
import pygame
from settings import *
from player import Player
from level import Level
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

game_state = "menu"  # ändra till menu när menu funkar

menu = Menu()  # skapa menu instans

player = Player(100, HEIGHT - 80)  # fixade y-positionen
level = Level("level1.txt")  # lägg till en level1.txt i samma mapp som main.py, eller ändra sökvägen här

attempts = 1 #denna verkar vara ute o cykla, låter den sitta kvar, den skadar inte
scroll_offset = 0 #kolla hur långt har scrollat

def reset_player(): #ny funktion hurraa!
    global scroll_offset
    player.rect.x = 100
    player.rect.y = HEIGHT - 80
    player.vel_y = 0
    scroll_offset = 0
    
    # återställer alla objekt
    # krävde ändringar i Level klassen för att spara originalpositioner
    # ladda om level, enklaste sättet o göra det på
    level.load_level("level1.txt")

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if game_state == "menu":
            if menu.start_button.is_clicked(event):
                game_state = "game"
                reset_player()  # reset när spelet startar
            elif menu.quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()
                
        elif game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                elif event.key == pygame.K_ESCAPE:  # gå tillbaka till meny
                    game_state = "menu"
    
    if game_state == "menu":
        menu.draw(screen) #självförklarligt
    
    if game_state == "game": 
        player.update(level.blocks)
        level.update(SCROLL_SPEED)
        scroll_offset += SCROLL_SPEED  # håller koll på hur långt scrollat
        
        for spike in level.spikes:  # för spike collisions 
            if player.rect.colliderect(spike.rect):
                reset_player()  # återställ spelaren
                    
        screen.fill(WHITE)
        level.draw(screen)
        player.draw(screen)
    
    pygame.display.flip()