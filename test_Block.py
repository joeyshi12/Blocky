import unittest
from model.Block import *


class TestBlock(unittest.TestCase):
    block: Block

    def setUp(self) -> None:
        display = pygame.display.set_mode((100, 100))
        self.block = Block(display, (0, 0))

    def test_update(self):
        self.block.update()
        self.assertEqual(self.block.x, 0)
        self.assertEqual(self.block.y, 0)

        self.block.dx = 10
        self.block.dy = 10
        self.block.update()

        self.assertEqual(self.block.x, 10)
        self.assertEqual(self.block.y, 10)
