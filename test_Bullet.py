import unittest

import pygame

from model.Bullet import Bullet


class TestBullet(unittest.TestCase):
    bullet: Bullet

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.bullet = Bullet(display, (96, 0), (3, 3))

    def test_update(self):
        self.bullet.update()
        self.assertEqual(self.bullet.rect.x, 99)
        self.assertEqual(self.bullet.rect.y, 3)
        self.assertEqual(self.bullet.dx, 3)
        self.assertEqual(self.bullet.dy, 3)

        self.bullet.update()
        self.assertEqual(self.bullet.rect.x, 102)
        self.assertEqual(self.bullet.rect.y, 6)
        self.assertEqual(self.bullet.dx, -3)
        self.assertEqual(self.bullet.dy, 3)

        self.bullet.update()
        self.assertEqual(self.bullet.rect.x, 99)
        self.assertEqual(self.bullet.rect.y, 9)
        self.assertEqual(self.bullet.dx, -3)
        self.assertEqual(self.bullet.dy, 3)
