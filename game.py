import pygame
import random

from ball import Ball
from basket import Basket
from level import Level

WIDTH, HEIGHT = 500, 700
FPS = 60
BALL_SPAWN_FREQUENCY = 180
HIGH_SCORE = 0

class Game:
    def __init__(self):
        global HIGH_SCORE
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Ball")
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()
        self.basket = Basket(WIDTH // 2, HEIGHT - 50)
        self.balls = []
        self.frame_count = 0
        self.start_time = pygame.time.get_ticks()
        self.time_limit = 60
        self.score = 0
        self.high_score = HIGH_SCORE
        self.font = pygame.font.Font(None, 36)

    def spawn_balls(self):
        num_balls = random.randint(1, 3)
        for _ in range(num_balls):
            x = random.randint(0, WIDTH - 40)
            color = random.choice(["orange", "blue", "red", "purple"])
            self.balls.append(Ball(x, -40, color))

    def run(self):
        global HIGH_SCORE
        while self.running:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
            remaining_time = max(0, self.time_limit - elapsed_time)

            if remaining_time == 0:
                self.running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.basket.switch_color()
            keys = pygame.key.get_pressed()
            self.basket.move(keys)

            self.frame_count += 1
            if self.frame_count % BALL_SPAWN_FREQUENCY == 0:
                self.spawn_balls()
            self.level.update()
            balls_to_remove = []

            for ball in self.balls[:]:
                ball.update()
                for obstacle in self.level.obstacles:
                    if ball.rect.colliderect(obstacle.rect):
                        ball.bounce(obstacle)


                if self.basket.catch_ball(ball):
                    if self.basket.colors[self.basket.current_color_index] == ball.color:
                        self.score += 10
                    else:
                        self.score -= 5
                    balls_to_remove.append(ball)


            for ball in balls_to_remove:
                if ball in self.balls:
                    self.balls.remove(ball)
            if self.score > HIGH_SCORE:
                HIGH_SCORE = self.score
            self.screen.fill((0, 0, 0))
            self.level.draw(self.screen)
            self.basket.draw(self.screen)
            for ball in self.balls:
                ball.draw(self.screen)
            self.draw_ui(remaining_time)

            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def draw_ui(self, time_left):
        timer_text = self.font.render(f"Time: {time_left}s", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 0))
        high_score_text = self.font.render(f"High Score: {HIGH_SCORE}", True, (0, 255, 0))

        self.screen.blit(timer_text, (20, 20))
        self.screen.blit(score_text, (20, 50))
        self.screen.blit(high_score_text, (20, 80))
