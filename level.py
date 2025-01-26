import pygame
from obstacle import Obstacle

class Level:
    def __init__(self):
        self.background = pygame.image.load("resources/backgroundOT.png")
        self.background = pygame.transform.scale(self.background, (500, 700))
        self.obstacles = []
        self.create_obstacles()

    def create_obstacles(self):
        positions = [
            [(90, 180), (250, 180), (410, 180)],
            [(100, 300), (250, 300), (400, 300), (550, 300)],
            [(90, 420), (250, 420), (410, 420)]
        ]

        for row in positions:
            for x, y in row:
                self.obstacles.append(Obstacle(x, y))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for obstacle in self.obstacles:
            obstacle.draw(screen)
