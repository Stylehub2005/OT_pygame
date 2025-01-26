import pygame

class Ball:
    def __init__(self, x, y, color):
        self.image = pygame.image.load(f"resources/{color}_ball.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)