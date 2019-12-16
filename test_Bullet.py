import unittest

import pygame
from pygame.surface import Surface

from model.Bullet import Bullet


class BulletTest(unittest.TestCase):
    display: Surface
    test_bullet: Bullet

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.test_bullet = Bullet(display)

    def test_update(self):
        self.test_bullet.set_x(96)
        self.test_bullet.set_y(0)
        self.test_bullet.set_vx(3)
        self.test_bullet.set_vy(3)

        self.assertEqual(self.test_bullet.x, 96)
        self.assertEqual(self.test_bullet.y, 0)
        self.assertEqual(self.test_bullet.vx, 3)
        self.assertEqual(self.test_bullet.vy, 3)

        self.test_bullet.update()
        self.assertEqual(self.test_bullet.x, 99)
        self.assertEqual(self.test_bullet.y, 3)
        self.assertEqual(self.test_bullet.vx, 3)
        self.assertEqual(self.test_bullet.vy, 3)

        self.test_bullet.update()
        self.assertEqual(self.test_bullet.x, 102)
        self.assertEqual(self.test_bullet.y, 6)
        self.assertEqual(self.test_bullet.vx, -3)
        self.assertEqual(self.test_bullet.vy, 3)

        self.test_bullet.update()
        self.assertEqual(self.test_bullet.x, 99)
        self.assertEqual(self.test_bullet.y, 9)
        self.assertEqual(self.test_bullet.vx, -3)
        self.assertEqual(self.test_bullet.vy, 3)
