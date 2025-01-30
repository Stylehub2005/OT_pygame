import random
import pygame

class Ball:
    def __init__(self, x, y, color):
        self.color = color
        self.image = pygame.image.load(f"resources/{color}_ball.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = 0
        self.speed_y = 2
        self.gravity = 0.1


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.speed_y += self.gravity


        if self.rect.left < 0 or self.rect.right > 500:
            self.speed_x = -self.speed_x * 0.8

    def bounce(self, obstacle):
        if self.rect.bottom > obstacle.rect.top and self.speed_y > 0:
            self.rect.bottom = obstacle.rect.top
            self.speed_y = -abs(self.speed_y) * 0.7
            self.speed_x += random.uniform(-1, 1)
        elif self.rect.top < obstacle.rect.bottom and self.speed_y < 0:
            self.rect.top = obstacle.rect.bottom
            self.speed_y = abs(self.speed_y) * 0.7
        elif self.rect.right > obstacle.rect.left and self.rect.left < obstacle.rect.right:
            self.speed_x = -self.speed_x * 0.7

    def draw(self, screen):
        screen.blit(self.image, self.rect)
