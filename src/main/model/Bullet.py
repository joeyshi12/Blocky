import random as rand

from pygame.surface import Surface


class Bullet:
    display: Surface
    x: int
    y: int
    vx: int = rand.randint(3, 5)
    vy: int = rand.randint(3, 5)
    radius: int = 10

    def __init__(self, display):
        self.display = display
        self.x = rand.randint(0, display.get_width())
        self.y = rand.randint(0, display.get_height())

    def set_vx(self, vx: int):
        self.vx = vx

    def set_vy(self, vy: int):
        self.vy = vy

    def update_bullet(self):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.set_vx(abs(self.vx))
        if self.display.get_width() < self.x:
            self.set_vx(-abs(self.vx))
        if self.y < 0:
            self.set_vy(abs(self.vy))
        if self.display.get_height() < self.y:
            self.set_vy(-abs(self.vy))