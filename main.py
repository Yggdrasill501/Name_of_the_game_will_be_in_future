# -*- coding: utf-8 -*-
"""Run whole project form here"""
import pygame
from sys import exit

game_active: bool = True

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active:
                print('Game is runing xD')
