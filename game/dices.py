# -*- coding: utf-8 -*-
"""File with algorythm of the dices"""
from random import randint
# from abc import abstractmethod


class DiceAlgorythm:
    """
    Class to get random two numbers from on the dices
    :return type: tuple(int,int)
    """
    def __init__(self) -> None:
        """Initialise"""
        self.dices: list
        self.dices = []

    @staticmethod
    def roll() -> int:
        """Method"""
        number = randint(1, 7)
        return int(number)

    def return_number(self) -> list:
        """Method"""
        for i in range(2):
            roll = self.roll()
            self.dices.append(roll)

        return self.dices
