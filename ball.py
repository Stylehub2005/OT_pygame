import random
import pygame

class Ball:
    animations = {
        "default": [pygame.image.load(f"resources/ball_anim/frame1_{i}.png") for i in range(6)],
        "black": [pygame.image.load(f"resources/black_anim/frame2_{i}.png") for i in range(2)],
        "gold": [pygame.image.load(f"resources/gold_anim/frame3_{i}.png") for i in range(6)],
    }

    def __init__(self, x, y, color):
        self.color = color
        self.original_image = pygame.image.load(f"resources/{color}_ball.png")
        self.original_image = pygame.transform.scale(self.original_image, (40, 40))
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = 0
        self.speed_y = 2
        self.gravity = 0.1
        self.animation_frames = self.get_animation_frames(color)
        self.current_frame = 0
        self.animating = False
        self.animation_speed = 1
        self.animation_counter = 0

    def get_animation_frames(self, color):
        if color == "black":
            return self.animations["black"]
        elif color == "gold":
            return self.animations["gold"]
        else:
            return self.animations["default"]

    def update(self):
        if self.animating:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.current_frame += 1
                if self.current_frame >= len(self.animation_frames):
                    self.animating = False
                    self.current_frame = 0
                    self.image = self.original_image
                else:
                    self.image = self.animation_frames[self.current_frame]
        else:
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

    def start_animation(self):
        self.animating = True
        self.current_frame = 0
        self.animation_counter = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
