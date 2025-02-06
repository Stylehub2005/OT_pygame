import pygame

class Basket:
    def __init__(self, x, y):
        self.colors = ["orange", "blue", "red", "purple","gold","black"]
        self.current_color_index = 0
        self.image = None
        self.rect = pygame.Rect(x, y, 80, 40)
        self.update_image()

    def update_image(self):
        color = self.colors[self.current_color_index]
        self.image = pygame.image.load(f"resources/basket_{color}.png")
        self.image = pygame.transform.scale(self.image, (80, 40))

    def switch_color(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)
        self.update_image()

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.x += 5

    def catch_ball(self, ball):
        return self.rect.colliderect(ball.rect)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
