"""
    Filename: main.py
    Description: This file is game enter file.

    Author: Botian Lan
    Date: 2022-2-7
"""

from source import setup
from source.states import main_menu


def main():
    game = setup.Game()
    main_menu.MainMenu()
    game.run()


if __name__ == "__main__":
    main()
    quit()
