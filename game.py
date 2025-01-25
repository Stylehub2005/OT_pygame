import pygame
from level import Level

WIDTH, HEIGHT = 400, 600
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Ball")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.level.update()
            self.level.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()