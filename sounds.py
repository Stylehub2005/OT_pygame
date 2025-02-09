import pygame

pygame.init()
pygame.mixer.init()


SOUNDS = {
    "background": "resources/sounds/background.mp3",
    "button": "resources/sounds/button.mp3",
    "catch": "resources/sounds/catch.mp3",
    "hit": "resources/sounds/hit.mp3",
    "miss": "resources/sounds/miss.mp3"
}


pygame.mixer.music.load(SOUNDS["background"])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)