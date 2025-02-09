
import pygame

from sounds import SOUNDS


class HUD:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background = pygame.image.load("resources/backgroundOT.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        pygame.font.init()

        self.font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 36)
        self.game_state = "menu"
        self.buttons = {
            "start": pygame.Rect(width // 2 - 75, height // 2 - 50, 150, 50),
            "exit": pygame.Rect(width // 2 - 75, height // 2 + 20, 150, 50),
            "restart": pygame.Rect(width // 2 - 75, height // 2 - 50, 150, 50),
        }

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))
        self.font = pygame.font.Font(None, 96)  # Double the font size (48 * 2)
        title_text = self.font.render("Hello", True, (255, 255, 255))
        self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, 180))
        self.draw_button("start", "Start")
        self.draw_button("exit", "Exit")

    def draw_game_over(self, score, high_score):
        self.screen.blit(self.background, (0, 0))

        # Текст "Game Over"
        game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, 150))

        # Отображение текущего счёта
        score_text = self.button_font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2, 230))

        # Отображение High Score
        high_score_text = self.button_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (self.width // 2 - high_score_text.get_width() // 2, 260))

        # Кнопки Restart и Exit
        self.draw_button("restart", "Restart")
        self.draw_button("exit", "Exit")

    def draw_button(self, button_key, text):
        button_rect = self.buttons[button_key]
        pygame.draw.rect(self.screen, (50, 50, 50), button_rect, border_radius=8)
        pygame.draw.rect(self.screen, (255, 255, 255), button_rect, 2, border_radius=8)

        button_text = self.button_font.render(text, True, (255, 255, 255))
        self.screen.blit(button_text, (
        button_rect.centerx - button_text.get_width() // 2, button_rect.centery - button_text.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if self.game_state == "menu":
                if self.buttons["start"].collidepoint(mouse_pos):
                    pygame.mixer.Sound(SOUNDS["button"]).play()  # Звук кнопки
                    self.game_state = "playing"
                elif self.buttons["exit"].collidepoint(mouse_pos):
                    pygame.mixer.Sound(SOUNDS["button"]).play()  # Звук кнопки
                    return "exit"
            elif self.game_state == "game_over":
                if self.buttons["restart"].collidepoint(mouse_pos):
                    pygame.mixer.Sound(SOUNDS["button"]).play()  # Звук кнопки
                    self.game_state = "playing"
                    return "restart"
                elif self.buttons["exit"].collidepoint(mouse_pos):
                    pygame.mixer.Sound(SOUNDS["button"]).play()  # Звук кнопки
                    return "exit"
