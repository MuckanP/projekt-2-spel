import sys
import pygame
from settings import *
from player import Player
from level import Level
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Clone")
clock = pygame.time.Clock()

game_state = "menu"

PLAYER_START_X = 100
PLAYER_START_Y = 200

player = Player(PLAYER_START_X, PLAYER_START_Y)
level = Level("level1.txt")
menu = Menu()

attempts = 1
font = pygame.font.SysFont(None, 36)

small_font = pygame.font.SysFont(None, 24) # font specifikt för "esc" texten

def get_camera(player_rect):
    cam_x = player_rect.centerx - WIDTH // 2
    cam_y = player_rect.centery - HEIGHT // 2
    return cam_x, cam_y

def reset_game():
    player.rect.x = PLAYER_START_X
    player.rect.y = PLAYER_START_Y
    player.vel_y = 0
    level.reset()

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
                reset_game()
                attempts = 1
            if menu.quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        elif game_state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    game_state = "menu"

    if game_state == "menu":
        menu.draw(screen)

    elif game_state == "game":
        # scrolla världen
        player.rect.x += SCROLL_SPEED
        player.update(level.blocks)
        level.update()

        # kollision för spikes
        for spike in level.spikes:
            if player.rect.colliderect(spike.rect):
                attempts += 1
                reset_game()
                break

        cam_x, cam_y = get_camera(player.rect)

        screen.fill(WHITE)
        level.draw(screen, cam_x, cam_y)
        player.draw(screen, cam_x, cam_y)

        esc_text = small_font.render("ESC to quit to menu", True, BLACK)
        screen.blit(esc_text, (1100, 10))  
        
        attempt_text = font.render(f"Attempt {attempts}", True, BLACK)
        screen.blit(attempt_text, (10, 10))

    pygame.display.flip()