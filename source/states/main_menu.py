"""
    Filename: main_menu.py
    Description: This file is abstract menu .

    Author: Botian Lan
    Date: 2022-2-7
"""
import source.utils as tools
import source.constants as c
from source import setup


class MainMenu:
    def __init__(self):
        self.backgroud()
        self.player()
        self.cursor()

    def backgroud(self):
        bg = setup.game_images['level_1']
        bg = tools.get_image(bg, 0, 0, c.SCREEN_W/c.BG_DIV, 224, (c.SCREEN_W, c.SCREEN_H), (0, 0, 0))
        setup.screen.blit(bg, (0, 0))

        title = setup.game_images['title_screen']
        title = tools.get_image(title, 1, 60, 176, 88, (176*3, 88*3), (255, 0, 220))
        setup.screen.blit(title, (237, 100))

    def player(self):
        mario = setup.game_images['mario_bros']
        mario = tools.get_image(mario, 178, 32, 12, 16, (12*4, 16*4), (0, 0, 0))
        setup.screen.blit(mario, (150, 470))

    def cursor(self):
        cursor = setup.game_images['item_objects']
        cursor = tools.get_image(cursor, 25, 160, 8, 8, (8*4, 8*4), (0, 0, 0))
        setup.screen.blit(cursor, (320, 400))


