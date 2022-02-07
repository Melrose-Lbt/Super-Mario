"""
    Filename: utils.py
    Description: This file contains many tools which game will use.

    Author: Botian Lan
    Date: 2022-2-7
"""
import os

import pygame.display
import source.constants as c
from source import setup
import source.states.main_menu as menu


# load image
def load_image(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    images = {}
    for img in os.listdir(path):
        name, ext = os.path.splitext(img)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, img))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            images[name] = img
    return images


# get image
def get_image(img, x, y, w, h, scale, color_key):
    sub_img = pygame.Surface((w, h))
    sub_img.blit(img, (0, 0), (x, y, w, h))
    sub_img.set_colorkey(color_key)
    sub_img = pygame.transform.scale(sub_img, (scale[0], scale[1]))
    return sub_img


if __name__ == "__main__":
    import setup
    path = '/Users/drcooper/Library/Mobile Documents/com~apple~CloudDocs/Code/CODE/PycharmProjects/' \
           'SuperMario/resources/graphics'
    imgs = load_image(path)
    print(imgs)

