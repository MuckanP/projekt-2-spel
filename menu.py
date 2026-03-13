# menu.py
import pygame
from settings import WIDTH, HEIGHT, WHITE, BLACK

class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, 40)
        self.text = self.font.render(text, True, BLACK)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        screen.blit(
            self.text,
            (
                self.rect.centerx - self.text.get_width() // 2,
                self.rect.centery - self.text.get_height() // 2,
            ),
        )

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class Menu: # knappar i menyn
    def __init__(self):
        self.font_big = pygame.font.SysFont(None, 90)

        self.background = pygame.image.load("background.png") # ladda in bakgrundsbilden
        self.background = pygame.transform.scale(self.background,(WIDTH,HEIGHT)) # skalera bakgrundsbilden till skärmstorleken
        
        self.start_button = Button( # startknapp
            "Start Game",
            WIDTH // 2 - 100,
            HEIGHT // 2 - 140,
            200,
            60,
        )

        self.quit_button = Button( # quitknapp
            "Quit",
            WIDTH // 2 - 100,
            HEIGHT // 2 - 70,
            200,
            60,
        )

    def draw(self, screen):
        screen.fill(WHITE)

        screen.blit(self.background, (0, 0))

        title = self.font_big.render("Kinesiska Geometry Dash", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3 - 90))

        self.start_button.draw(screen)
        self.quit_button.draw(screen)