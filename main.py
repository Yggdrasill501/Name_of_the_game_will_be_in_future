# -*- coding: utf-8 -*-
"""Run whole project form here"""
import pygame
from sys import exit

game_active: bool = True
game_is_running: bool = True

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    background = pygame.image.load('')

    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                print('Game is running xD')
