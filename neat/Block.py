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
    isAlive: bool
    timeAlive: int = 0

    def __init__(self, display: Surface, pos: tuple, bullets: list):
        self.display = display
        self.rect = Rect(pos, (self.WIDTH, self.HEIGHT))
        self.bullets = bullets
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        self.isAlive = True

    def update(self):
        """updates block position"""
        self.timeAlive += 0.01
        if self.hasCollided():
            self.isAlive = False
        if self.moveUp:
            if self.rect.y > 0:
                self.rect.y -= self.SPEED
        if self.moveDown:
            if self.rect.y + self.HEIGHT < self.display.get_height():
                self.rect.y += self.SPEED
        if self.moveLeft:
            if self.rect.x > 0:
                self.rect.x -= self.SPEED
        if self.moveRight:
            if self.rect.x + self.WIDTH < self.display.get_width():
                self.rect.x += self.SPEED

    def hasCollided(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet):
                return True
        return False

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.display, self.COLOUR, self.rect)

    def getData(self):
        data = [self.rect.x, self.rect.y]
        for bullet in self.bullets:
            data.append((self.rect.x - bullet.rect.x) ** 2 + (self.rect.y - bullet.rect.y) ** 2)
        return data
