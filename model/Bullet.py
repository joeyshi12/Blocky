import pygame
from pygame.rect import Rect
from pygame.surface import Surface


class Bullet:
    RADIUS: int = 10
    COLOUR: tuple = (100, 100, 255)

    display: Surface
    rect: Rect
    dx: int
    dy: int

    def __init__(self, display: Surface, pos: tuple, vel: tuple):
        self.display = display
        self.rect = Rect(pos, (int(self.RADIUS * 1.5), int(self.RADIUS * 1.5)))
        self.dx, self.dy = vel

    def update(self):
        """updates bullet position by adding vx to x and vy to y;
        if bullet hits wall, its velocity is reflected"""
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x < 0:
            self.dx = abs(self.dx)
        if self.rect.x > self.display.get_width():
            self.dx = -abs(self.dx)
        if self.rect.y < 0:
            self.dy = abs(self.dy)
        if self.rect.y > self.display.get_height():
            self.dy = -abs(self.dy)

    def draw(self):
        """draws bullet on display"""
        pygame.draw.circle(self.display, self.COLOUR,
                           (int(self.rect.x + self.rect.width / 2), int(self.rect.y + self.rect.height / 2)),
                           self.RADIUS)
