from pygame.surface import Surface

from model.Observer import Observer


class Bullet(Observer):
    display: Surface
    x: int
    y: int
    vx: int
    vy: int
    radius: int = 10

    def __init__(self, pos: tuple, vel: tuple):
        self.x, self.y = pos
        self.vx, self.vy = vel

    def set_vx(self, vx: int):
        self.vx = vx

    def set_vy(self, vy: int):
        self.vy = vy

    def update(self, display: Surface):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy
        if self.x < 0:
            self.set_vx(abs(self.vx))
        if display.get_width() < self.x:
            self.set_vx(-abs(self.vx))
        if self.y < 0:
            self.set_vy(abs(self.vy))
        if display.get_height() < self.y:
            self.set_vy(-abs(self.vy))
