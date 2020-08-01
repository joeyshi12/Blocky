import unittest
from model.block import *


class TestBlock(unittest.TestCase):
    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.block = Block(display, (0, 0))

    def test_update(self):
        self.block.update()
        self.assertEqual(self.block.rect.x, 0)
        self.assertEqual(self.block.rect.y, 0)

        self.block.move_right = True
        self.block.update()
        self.assertEqual(self.block.rect.x, self.block.SPEED)
        self.assertEqual(self.block.rect.y, 0)

        self.block.move_right = False
        self.block.move_down = True
        self.block.update()
        self.assertEqual(self.block.rect.x, self.block.SPEED)
        self.assertEqual(self.block.rect.y, self.block.SPEED)

        self.block.move_down = False
        self.block.move_left = True
        self.block.update()
        self.assertEqual(self.block.rect.x, 0)
        self.assertEqual(self.block.rect.y, self.block.SPEED)

        self.block.move_left = False
        self.block.move_up = True
        self.block.update()
        self.assertEqual(self.block.rect.x, 0)
        self.assertEqual(self.block.rect.y, 0)

        self.block.update()
        self.assertEqual(self.block.rect.x, 0)
        self.assertEqual(self.block.rect.y, 0)

        self.block.move_left = True
        self.block.update()
        self.assertEqual(self.block.rect.x, 0)
        self.assertEqual(self.block.rect.y, 0)
