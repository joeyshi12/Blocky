import pygame
import random


class Bullet:
    RADIUS: int = 10
    COLOUR: tuple = (100, 100, 255)
    BULLET_VELOCITIES = [4, 5]

    surface: pygame.Surface
    rect: pygame.Rect
    dx: int
    dy: int

    def __init__(self, surface: pygame.Surface, pos: tuple = None, vel: tuple = None):
        self.surface = surface

        if pos is None:
            x = random.choice([random.randint(0, surface.get_width() // 4),
                               random.randint(3 * surface.get_width() // 4, surface.get_width() - 1)])
            y = random.choice([random.randint(0, surface.get_height() // 4),
                               random.randint(3 * surface.get_height() // 4, surface.get_height() - 1)])
            self.rect = pygame.Rect((x, y), (3 * self.RADIUS // 2, 3 * self.RADIUS // 2))
        else:
            self.rect = pygame.Rect(pos, (3 * self.RADIUS // 2, 3 * self.RADIUS // 2))

        if vel is None:
            self.dx = (1 if random.random() > 0.5 else -1) * random.choice(self.BULLET_VELOCITIES)
            self.dy = (1 if random.random() > 0.5 else -1) * random.choice(self.BULLET_VELOCITIES)
        else:
            self.dx, self.dy = vel

    def update(self):
        """updates bullet position by adding vx to x and vy to y;
        if bullet hits wall, its velocity is reflected"""
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x < 0:
            self.dx = abs(self.dx)
        if self.rect.x > self.surface.get_width():
            self.dx = -abs(self.dx)
        if self.rect.y < 0:
            self.dy = abs(self.dy)
        if self.rect.y > self.surface.get_height():
            self.dy = -abs(self.dy)

    def draw(self):
        """draws bullet on display"""
        pygame.draw.circle(self.surface, self.COLOUR,
                           (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                           self.RADIUS)
