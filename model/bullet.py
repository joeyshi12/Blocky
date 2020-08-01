import pygame
import random


class Bullet:
    RADIUS: int = 10
    COLOUR: tuple = (100, 100, 255)
    BULLET_VELOCITIES = [4, 5, 6]

    surface: pygame.Surface
    rect: pygame.Rect
    vx: int
    vy: int

    def __init__(self, surface: pygame.Surface, pos: tuple = None, vel: tuple = None):
        self.surface = surface
        pos = self.rand_pos() if pos is None else pos
        self.rect = pygame.Rect(pos, (3 * self.RADIUS // 2, 3 * self.RADIUS // 2))
        self.vx, self.vy = self.rand_vel() if vel is None else vel

    def rand_pos(self):
        x = random.choice([random.randint(0, self.surface.get_width() // 4),
                           random.randint(3 * self.surface.get_width() // 4, self.surface.get_width() - 1)])
        y = random.choice([random.randint(0, self.surface.get_height() // 4),
                           random.randint(3 * self.surface.get_height() // 4, self.surface.get_height() - 1)])
        return x, y

    def rand_vel(self):
        return (1 if random.random() > 0.5 else -1) * random.choice(self.BULLET_VELOCITIES), \
               (1 if random.random() > 0.5 else -1) * random.choice(self.BULLET_VELOCITIES)

    def randomize(self):
        self.rect.topleft = self.rand_pos()
        self.vx, self.vy = self.rand_vel()

    def update(self):
        """updates bullet position by adding vx to x and vy to y;
        if bullet hits wall, its velocity is reflected"""
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x < 0:
            self.vx = abs(self.vx)
        if self.rect.x > self.surface.get_width():
            self.vx = -abs(self.vx)
        if self.rect.y < 0:
            self.vy = abs(self.vy)
        if self.rect.y > self.surface.get_height():
            self.vy = -abs(self.vy)

    def draw(self):
        """draws bullet on display"""
        pygame.draw.circle(self.surface, self.COLOUR,
                           (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                           self.RADIUS)
