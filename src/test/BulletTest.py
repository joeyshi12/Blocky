import unittest

import pygame
from pygame.surface import Surface

from src.main.model.Bullet import Bullet


class BulletTest(unittest.TestCase):
    display: Surface
    test_bullet: Bullet

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.test_bullet = Bullet(display)

    def test_update(self):
        self.test_bullet.update()
        self.assertEquals(self.test_bullet.x, 0)
        self.assertEquals(self.test_bullet.y, 0)

        self.test_bullet.set_vx(10)
        self.test_bullet.set_vy(10)
        self.test_bullet.update()

        self.assertEquals(self.test_bullet.x, 10)
        self.assertEquals(self.test_bullet.y, 10)
