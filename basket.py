import pygame

class Basket:
    def __init__(self, x, y):
        self.image = pygame.image.load("resources/basket.png")
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 500:
            self.rect.x += 5

    def draw(self, screen):
        screen.blit(self.image, self.rect)