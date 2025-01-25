import pygame

class Level:
    def __init__(self):
        self.background = pygame.image.load("resources/backgroundOT.png")
        self.background = pygame.transform.scale(self.background, (400, 600))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background, (0, 0))