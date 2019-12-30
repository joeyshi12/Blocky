import pygame
from pygame.surface import Surface


class Block:
    display: Surface
    x: float
    y: float
    vx: float
    vy: float
    height: int
    width: int
    colour: tuple

    def __init__(self, display: Surface, pos: tuple, width: int, height: int, colour: tuple):
        self.display = display
        self.x, self.y = pos
        self.vx, self.vy = (0, 0)
        self.width = width
        self.height = height
        self.colour = colour

    def update(self):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.display, self.colour,
                         (self.x, self.y, self.width, self.height), 0)
