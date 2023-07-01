# -*- coding: utf-8 -*-
"""Player """
import pygame
from abc import abstractmethod


class Player(pygame.sprite.Sprite):
    """Class for player"""

    def __init__(self) -> None:
        """Init"""
        super().__init__()

    @abstractmethod
    def player_import(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pass

