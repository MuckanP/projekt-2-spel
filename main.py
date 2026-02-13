import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

attempts = 1

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
    
    for spike in level.spikes:
        if player.rect.colliderect(spike.rect):
            attempts + 1
            print("Attempt " attempts)