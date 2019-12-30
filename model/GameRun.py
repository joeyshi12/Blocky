import random as rand

import pygame
from pygame.surface import Surface

from model.Block import Block
from model.Bullet import Bullet
from model.Subject import Subject


class GameRun(Subject):
    BLOCK_WIDTH: int = 80
    BLOCK_HEIGHT: int = 60
    BLOCK_COLOUR: tuple = (0, 0, 0)
    NUMBER_OF_BULLETS: int = 3
    BULLET_VELOCITIES: list = [-8, -7, -6, 6, 7, 8]
    display: Surface

    def __init__(self, display: Surface):
        self.display = display
        self.block = Block(display,
                           (display.get_width() / 2 - self.BLOCK_WIDTH / 2,
                            display.get_height() / 2 - self.BLOCK_HEIGHT / 2),
                           self.BLOCK_WIDTH, self.BLOCK_HEIGHT, self.BLOCK_COLOUR)
        self.initialize_bullets(display)

    def initialize_bullets(self, display: Surface):
        """creates NUMBER_OF_BULLETS of bullets with random movement fields"""
        for i in range(self.NUMBER_OF_BULLETS):
            bullet_x = rand.randint(0, display.get_width())
            bullet_y = rand.randint(0, display.get_height())
            bullet_vx = rand.choice(self.BULLET_VELOCITIES)
            bullet_vy = rand.choice(self.BULLET_VELOCITIES)
            bullet = Bullet(display, (bullet_x, bullet_y), (bullet_vx, bullet_vy))
            self.add_observer(bullet)

    def collide_wall(self) -> bool:
        return self.block.x < 0 or self.block.x + self.block.width > self.display.get_width() or \
               self.block.y < 0 or self.block.y + self.block.height > self.display.get_height()

    def collide_bullet(self) -> bool:
        for bullet in self.observers:
            if self.block.x <= bullet.x <= self.block.x + self.block.width and \
                    self.block.y <= bullet.y <= self.block.y + self.block.height:
                return True
        return False

    def is_game_over(self) -> bool:
        """returns true if block collides with wall or bullet"""
        return self.collide_wall() or self.collide_bullet()

    def reset(self):
        """resets block to center position with 0 velocity and randomizes bullet movement fields"""
        self.block.x = self.display.get_width() / 2 - self.BLOCK_WIDTH / 2
        self.block.y = self.display.get_height() / 2 - self.BLOCK_HEIGHT / 2
        self.block.vx = 0
        self.block.vy = 0
        for bullet in self.observers:
            bullet.x = rand.randint(0, self.display.get_width())
            bullet.y = rand.randint(0, self.display.get_height())
            bullet.vx = rand.choice(self.BULLET_VELOCITIES)
            bullet.vy = rand.choice(self.BULLET_VELOCITIES)

    def update_game(self):
        """updates game state"""
        self.block.update()
        self.notify_observers()

    def draw(self):
        """draws display for game-loop"""
        self.block.draw()
        for bullet in self.observers:
            bullet.draw()

    def key_handle_down(self, key: str):
        """updates the velocity of block based on the key pressed down"""
        if key == pygame.K_w:
            self.block.vy = -6
        elif key == pygame.K_a:
            self.block.vx = -6
        elif key == pygame.K_s:
            self.block.vy = 6
        elif key == pygame.K_d:
            self.block.vx = 6

    def key_handle_up(self, key: str):
        """for any direction, if the block has velocity in the same direction as its corresponding key, then
        the velocity in that direction is set back to 0"""
        if key == pygame.K_w and self.block.vy == -6:
            self.block.vy = 0
        elif key == pygame.K_a and self.block.vx == -6:
            self.block.vx = 0
        elif key == pygame.K_s and self.block.vy == 6:
            self.block.vy = 0
        elif key == pygame.K_d and self.block.vx == 6:
            self.block.vx = 0
