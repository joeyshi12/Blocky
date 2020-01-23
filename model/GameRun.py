import random as rand

import pygame
from pygame.surface import Surface

from model.Block import Block
from model.Bullet import Bullet
from model.Score import Score
from model.Subject import Subject


class GameRun(Subject):
    BLOCK_VELOCITY: int = 6
    BULLET_VELOCITIES: list = list(range(-10, 9)) + list(range(2,10))

    display: Surface
    score: Score

    def __init__(self, display: Surface):
        self.display = display
        self.score = Score(display)
        self.block = Block(display, (display.get_width() / 2 - Block.WIDTH / 2,
                                     display.get_height() / 2 - Block.HEIGHT / 2))
        self.initialize_bullets()

    def initialize_bullets(self):
        """creates NUMBER_OF_BULLETS of bullets with random movement fields"""
        rand_int = rand.randrange(2, 5, 1)
        for i in range(rand_int):
            bullet_x = rand.randint(0, self.display.get_width())
            bullet_y = rand.randint(0, self.display.get_height())
            bullet_dx = rand.choice(self.BULLET_VELOCITIES)
            bullet_dy = rand.choice(self.BULLET_VELOCITIES)
            bullet = Bullet(self.display, (bullet_x, bullet_y), (bullet_dx, bullet_dy))
            self.add_observer(bullet)

    def collide_wall(self) -> bool:
        return self.block.rect.x < 0 or self.block.rect.x + self.block.WIDTH > self.display.get_width() or \
               self.block.rect.y < 0 or self.block.rect.y + self.block.HEIGHT > self.display.get_height()

    def collide_bullet(self) -> bool:
        for bullet in self.observers:
            if self.block.rect.colliderect(bullet.rect):
                return True
        return False

    def is_game_over(self) -> bool:
        """returns true if block collides with wall or bullet"""
        return self.collide_wall() or self.collide_bullet()

    def reset(self):
        """resets block to center position with 0 velocity and randomizes bullet movement fields"""
        self.score.current_score = 0
        self.block.rect.x = self.display.get_width() / 2 - self.block.WIDTH / 2
        self.block.rect.y = self.display.get_height() / 2 - self.block.HEIGHT / 2
        self.block.dx = 0
        self.block.dy = 0
        self.observers.clear()
        self.initialize_bullets()

    def update(self):
        """updates game state"""
        self.score.update()
        self.block.update()
        self.notify_observers()

    def render(self):
        """draws display for game-loop"""
        self.score.draw()
        self.block.draw()
        for bullet in self.observers:
            bullet.draw()

    def key_handle_down(self, key: int):
        """updates the velocity of block based on the key pressed down"""
        if key == pygame.K_w:
            self.block.dy = -self.BLOCK_VELOCITY
        elif key == pygame.K_a:
            self.block.dx = -self.BLOCK_VELOCITY
        elif key == pygame.K_s:
            self.block.dy = self.BLOCK_VELOCITY
        elif key == pygame.K_d:
            self.block.dx = self.BLOCK_VELOCITY

    def key_handle_up(self, key: int):
        """for any direction, if the block has velocity in the same direction as its corresponding key, then
        the velocity in that direction is set back to 0"""
        if key == pygame.K_w and self.block.dy == -self.BLOCK_VELOCITY:
            self.block.dy = 0
        elif key == pygame.K_a and self.block.dx == -self.BLOCK_VELOCITY:
            self.block.dx = 0
        elif key == pygame.K_s and self.block.dy == self.BLOCK_VELOCITY:
            self.block.dy = 0
        elif key == pygame.K_d and self.block.dx == self.BLOCK_VELOCITY:
            self.block.dx = 0
