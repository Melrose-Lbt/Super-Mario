"""
    Filename: setup.py
    Description: This file provides initialization function for game.

    Author: Botian Lan
    Date: 2022-2-7
"""
import pygame
import source.constants as c
from source.utils import load_image

pygame.init()
pygame.display.set_mode((c.SCREEN_W, c.SCREEN_H))
pygame.display.set_caption('Super Mario v-1.0.0')
game_images = load_image(c.IMG_PATH)
screen = pygame.display.get_surface()


class Game:
    def __init__(self):
        self.screen = screen

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
            pygame.display.update()



