import pygame
import random
from ball import Ball
from basket import Basket
from level import Level
from HUD import HUD

WIDTH, HEIGHT = 500, 700
FPS = 60
BALL_SPAWN_FREQUENCY = 180
HIGH_SCORE = 0


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Ball")
        self.clock = pygame.time.Clock()
        self.hud = HUD(self.screen, WIDTH, HEIGHT)
        self.running = True
        self.level = Level()
        self.basket = Basket(WIDTH // 2, HEIGHT - 50)
        self.balls = []
        self.frame_count = 0
        self.start_time = pygame.time.get_ticks()
        self.time_limit = 60
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.color_switching = False
        self.basket_disabled_until = 0
        self.double_score_until = 0

    def spawn_balls(self):
        num_balls = random.randint(1, 5)
        for _ in range(num_balls):
            x = random.randint(0, WIDTH - 40)
            color = random.choice(["orange", "blue", "red", "purple", "gold", "black"])
            self.balls.append(Ball(x, -40, color))

    def run(self):
        global HIGH_SCORE
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                hud_action = self.hud.handle_event(event)
                if hud_action == "exit":
                    self.running = False
                elif hud_action == "restart":
                    self.reset_game()

            self.screen.blit(self.level.background, (0, 0))

            if self.hud.game_state == "menu":
                self.hud.draw_menu()
            elif self.hud.game_state == "playing":
                self.update_game()
            elif self.hud.game_state == "game_over":
                self.hud.draw_game_over(self.score)

            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def update_game(self):
        global HIGH_SCORE
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        remaining_time = max(0, self.time_limit - elapsed_time)

        if remaining_time == 0:
            self.hud.game_state = "game_over"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.color_switching:
            self.basket.switch_color()
            self.color_switching = True
        if not keys[pygame.K_SPACE]:
            self.color_switching = False

        if pygame.time.get_ticks() > self.basket_disabled_until:
            self.basket.move(keys)

        self.frame_count += 1
        if self.frame_count % BALL_SPAWN_FREQUENCY == 0:
            self.spawn_balls()

        self.level.update()



        for ball in self.balls:
            if ball.to_remove:
                self.balls.remove(ball)


            for obstacle in self.level.obstacles:
                if ball.rect.colliderect(obstacle.rect):
                    ball.bounce(obstacle)

            if self.basket.catch_ball(ball):

                ball.explode_ball()
                if ball.color == "black":
                    self.basket_disabled_until = pygame.time.get_ticks() + 5000

                elif ball.color == "gold":
                    self.double_score_until = pygame.time.get_ticks() + 10000
                else:
                    score_multiplier = 2 if pygame.time.get_ticks() < self.double_score_until else 1
                    if self.basket.colors[self.basket.current_color_index] == ball.color:
                        self.score += 10 * score_multiplier


                    else:
                        self.score -= 5
                        

                break


            if ball.rect.bottom >= HEIGHT-20:
                ball.explode_ball()



        if self.score > HIGH_SCORE:
            HIGH_SCORE = self.score


        self.screen.blit(self.level.background, (0, 0))
        self.level.draw(self.screen)
        self.basket.draw(self.screen)
        for ball in self.balls:
            ball.update()
            ball.draw(self.screen)
        self.draw_ui(remaining_time)

    def reset_game(self):
        self.level = Level()
        self.basket = Basket(WIDTH // 2, HEIGHT - 50)
        self.balls = []
        self.frame_count = 0
        self.start_time = pygame.time.get_ticks()
        self.score = 0
        self.hud.game_state = "playing"
        self.basket_disabled_until = 0
        self.double_score_until = 0

    def draw_ui(self, time_left):
        timer_text = self.font.render(f"Time: {time_left}s", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 0))
        high_score_text = self.font.render(f"High Score: {HIGH_SCORE}", True, (0, 255, 0))

        self.screen.blit(timer_text, (20, 20))
        self.screen.blit(score_text, (20, 50))
        self.screen.blit(high_score_text, (20, 80))