import pygame
from pygame import Surface, Rect

class Block:
    WIDTH: int = 80
    HEIGHT: int = 60
    COLOUR: tuple = (255, 0, 0)
    SPEED: int = 6

    display: Surface
    rect: Rect
    bullets: list
    moveUp: bool
    moveDown: bool
    moveLeft: bool
    moveRight: bool

    def __init__(self, display: Surface, pos: tuple, bullets: list):
        self.display = display
        self.rect = Rect(pos, (self.WIDTH, self.HEIGHT))
        self.bullets = bullets
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False

    def update(self):
        """updates block position"""
        if self.moveUp:
            self.rect.y -= self.SPEED
        if self.moveDown:
            self.rect.y += self.SPEED
        if self.moveLeft:
            self.rect.x -= self.SPEED
        if self.moveRight:
            self.rect.x += self.SPEED

    def hasCollided(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet):
                return True
        return self.rect.x < 0 or self.rect.x + self.WIDTH > self.display.get_width() or \
               self.rect.y < 0 or self.rect.y + self.HEIGHT > self.display.get_height()

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.display, self.COLOUR, self.rect)
