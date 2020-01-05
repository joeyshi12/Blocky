import unittest

import pygame
from pygame.surface import Surface

from model.GameRun import GameRun

pygame.init()


class TestGameRun(unittest.TestCase):
    game_run: GameRun

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.game_run = GameRun(display)

    def test_initialize_bullets(self):
        for bullet in self.game_run.observers:
            self.assertTrue(0 <= bullet.rect.x <= self.game_run.display.get_width())
            self.assertTrue(0 <= bullet.rect.y <= self.game_run.display.get_height())
            self.assertTrue(bullet.dx in self.game_run.BULLET_VELOCITIES)
            self.assertTrue(bullet.dy in self.game_run.BULLET_VELOCITIES)

    def test_collide_wall_left(self):
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.x = 0
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.x -= 1
        self.assertTrue(self.game_run.collide_wall())

    def test_collide_wall_right(self):
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.x = self.game_run.display.get_width() - self.game_run.block.WIDTH
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.x += 1
        self.assertTrue(self.game_run.collide_wall())

    def test_collide_wall_up(self):
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.y = 0
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.y -= 1
        self.assertTrue(self.game_run.collide_wall())

    def test_collide_wall_down(self):
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.y = self.game_run.display.get_height() - self.game_run.block.HEIGHT
        self.assertFalse(self.game_run.collide_wall())
        self.game_run.block.rect.y += 1
        self.assertTrue(self.game_run.collide_wall())
