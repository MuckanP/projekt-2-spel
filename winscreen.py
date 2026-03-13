# win_screen.py
import pygame
from settings import WIDTH, HEIGHT, WHITE, BLACK, GREEN, BLUE

class WinScreen:
    def __init__(self):
        self.font_big = pygame.font.SysFont(None, 100)
        self.font_medium = pygame.font.SysFont(None, 50)
        self.font_small = pygame.font.SysFont(None, 30)
        
        # knapp för att gå tillbaka till menyn
        self.menu_button = Button(
            "Back to Menu",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 80,
            200,
            60
        )
        
    def draw(self, screen, attempts):
        # semitransparent bakgrund
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((50, 50, 50))
        screen.blit(overlay, (0, 0))
        
        # skriv ut "YOU WIN!" texten
        win_text = self.font_big.render("YOU WIN!", True, GREEN)
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(win_text, win_rect)
        
        # skriv ut
        attempts_text = self.font_medium.render(f"Attempts: {attempts}", True, WHITE)
        attempts_rect = attempts_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(attempts_text, attempts_rect)
        
        # rendera menyknappen
        self.menu_button.draw(screen)
        
    def handle_event(self, event):
        return self.menu_button.is_clicked(event)


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