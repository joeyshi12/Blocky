import pygame
from pygame.surface import Surface


class Block:
    WIDTH: int = 80
    HEIGHT: int = 60
    COLOUR: tuple = (255, 0, 0)
    display: Surface
    x: int
    y: int
    vx: int
    vy: int

    def __init__(self, display: Surface, pos: tuple):
        self.display = display
        self.x, self.y = pos
        self.vx, self.vy = (0, 0)

    def update(self):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.display, self.COLOUR,
                         (self.x, self.y, self.WIDTH, self.HEIGHT), 0)
