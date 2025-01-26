import random

import pygame
from level import Level
from basket import Basket
from ball import Ball


WIDTH, HEIGHT = 400, 600
FPS = 60
BALL_SPAWN_FREQUENCY = 30

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Ball")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()
        self.basket = Basket(WIDTH // 2, HEIGHT - 20)
        self.balls = []
        self.frame_count = 0

    def spawn_balls(self):
        num_balls = random.randint(1, 4)
        for _ in range(num_balls):
            x = random.randint(0, WIDTH - 40)
            color = random.choice(["orange", "blue", "red", "purple"])
            self.balls.append(Ball(x, -40, color))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            keys = pygame.key.get_pressed()
            self.basket.move(keys)


            self.frame_count += 1
            if self.frame_count % BALL_SPAWN_FREQUENCY == 0:
                self.spawn_balls()


            self.level.update()
            for ball in self.balls:
                ball.update()

            self.level.draw(self.screen)
            self.basket.draw(self.screen)
            for ball in self.balls:
                ball.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()