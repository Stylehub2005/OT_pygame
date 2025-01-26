import pygame

class Obstacle:
    def __init__(self, x, y):
        self.image = pygame.image.load("resources/obstacle.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)