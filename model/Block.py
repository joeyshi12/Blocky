import pygame
from pygame import Surface, Rect


class Block:
    WIDTH: int = 80
    HEIGHT: int = 60
    COLOUR: tuple = (255, 0, 0)

    display: Surface
    rect: Rect
    dx: int
    dy: int

    def __init__(self, display: Surface, pos: tuple):
        self.display = display
        self.rect = Rect(pos, (self.WIDTH, self.HEIGHT))
        self.dx, self.dy = (0, 0)

    def update(self):
        """updates block position by adding vx to x and vy to y"""
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.display, self.COLOUR, self.rect)
