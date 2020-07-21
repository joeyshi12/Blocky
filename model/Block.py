import pygame
import numpy as np


class Block:
    WIDTH: int = 50
    HEIGHT: int = 50
    COLOUR: tuple = (255, 0, 0)
    SPEED: int = 4

    surface: pygame.Surface
    rect: pygame.Rect
    bullets: list
    move_up: bool = False
    move_down: bool = False
    move_left: bool = False
    move_right: bool = False
    is_alive: bool = True

    def __init__(self, surface: pygame.Surface, pos: tuple, bullets: list, network=None):
        self.surface = surface
        self.rect = pygame.Rect(pos, (self.WIDTH, self.HEIGHT))
        self.bullets = bullets
        self.network = network

    def update(self):
        """updates block position"""
        if self.check_collision():
            self.is_alive = False
        if self.move_up:
            if self.rect.y > 0:
                self.rect.y -= self.SPEED
        if self.move_down:
            if self.rect.y + self.HEIGHT < self.surface.get_height():
                self.rect.y += self.SPEED
        if self.move_left:
            if self.rect.x > 0:
                self.rect.x -= self.SPEED
        if self.move_right:
            if self.rect.x + self.WIDTH < self.surface.get_width():
                self.rect.x += self.SPEED

    def check_collision(self):
        return self.check_collide_wall() or self.check_collide_bullet()

    def check_collide_wall(self):
        return self.rect.y <= 0 or self.rect.y + self.HEIGHT >= self.surface.get_height() or self.rect.x <= 0 or self.rect.x + self.WIDTH >= self.surface.get_width()

    def check_collide_bullet(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet):
                return True
        return False

    def draw(self):
        """draws block on display"""
        pygame.draw.rect(self.surface, self.COLOUR, self.rect)

    def predict(self):
        """make prediction from input data using self.network"""
        inputs = list()
        inputs.append(self.rect.x / self.surface.get_width())
        inputs.append(self.rect.y / self.surface.get_height())
        for i in range(len(self.bullets)):
            dx = self.rect.x - self.bullets[i].rect.x
            dy = self.rect.y - self.bullets[i].rect.y
            inputs.append(np.sqrt((dx ** 2 + dy ** 2) /
                                  (self.surface.get_width() ** 2 + self.surface.get_height() ** 2)))
            inputs.append(dx / self.surface.get_width())
            inputs.append(dy / self.surface.get_height())
            inputs.append(self.bullets[i].dx / 6)
            inputs.append(self.bullets[i].dy / 6)

        action = self.network.activate(inputs)
        i = action.index(max(action))

        # i == 0: right         i == 4: left
        # i == 1: up + right    i == 5: down + left
        # i == 2: up            i == 6: down
        # i == 3: left + up     i == 7: right + down
        self.move_up = i == 1 or i == 2 or i == 3
        self.move_down = i == 5 or i == 6 or i == 7
        self.move_left = i == 3 or i == 4 or i == 5
        self.move_right = i == 0 or i == 1 or i == 7

