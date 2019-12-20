import unittest
from model.Block import *


class TestBlock(unittest.TestCase):
    test_block: Block

    def setUp(self) -> None:
        self.test_block = Block((0, 0), 20, 30, (0, 0, 0))

    def test_update(self):
        self.test_block.update()
        self.assertEqual(self.test_block.x, 0)
        self.assertEqual(self.test_block.y, 0)

        self.test_block.vx = 10
        self.test_block.vy = 10
        self.test_block.update()

        self.assertEqual(self.test_block.x, 10)
        self.assertEqual(self.test_block.y, 10)
