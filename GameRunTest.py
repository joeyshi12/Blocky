import unittest

import pygame

from model.GameRun import GameRun


class GameRunTest(unittest.TestCase):
    test_gameRun: GameRun

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.test_gameRun = GameRun(display)

    # TODO: write some tests
