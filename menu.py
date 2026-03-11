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


class Menu:
    def __init__(self):
        self.font_big = pygame.font.SysFont(None, 72)

        self.start_button = Button(
            "Start Game",
            WIDTH // 2 - 100,
            HEIGHT // 2,
            200,
            60,
        )

        self.quit_button = Button(
            "Quit",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 80,
            200,
            60,
        )

    def draw(self, screen):
        screen.fill(WHITE)

        title = self.font_big.render("Geometry Dash Clone", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))

        self.start_button.draw(screen)
        self.quit_button.draw(screen)