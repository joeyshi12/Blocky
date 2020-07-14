import random as rand

import pygame
from pygame.surface import Surface

from model.Block import Block
from model.Bullet import Bullet
from model.Score import Score


class GameRun:
    BULLET_VELOCITIES: list = list(range(-8, -4)) + list(range(4, 8))
    num_bullets: int = 3
    bullets: list = []
    display: Surface
    score: Score

    def __init__(self, display: Surface):
        self.display = display
        self.score = Score(display)
        self.block = Block(display, (display.get_width() // 2 - Block.WIDTH // 2, display.get_height() // 2 - Block.HEIGHT // 2), self.bullets)
        self.initialize_bullets()

    def initialize_bullets(self):
        """creates num_bullets of bullets with random movement fields"""
        for i in range(self.num_bullets):
            bullet_x = rand.choice([rand.randint(0, self.display.get_width() // 4), rand.randint(3 * self.display.get_width() // 4, self.display.get_width())])
            bullet_y = rand.choice([rand.randint(0, self.display.get_height() // 4), rand.randint(3 * self.display.get_height() // 4, self.display.get_height())])
            bullet_dx = rand.choice(self.BULLET_VELOCITIES)
            bullet_dy = rand.choice(self.BULLET_VELOCITIES)
            bullet = Bullet(self.display, (bullet_x, bullet_y), (bullet_dx, bullet_dy))
            self.bullets.append(bullet)

    def reset(self):
        """resets block to center position with 0 velocity and randomizes bullet movement fields"""
        self.score.current_score = 0
        self.block.rect.x = self.display.get_width() / 2 - self.block.WIDTH / 2
        self.block.rect.y = self.display.get_height() / 2 - self.block.HEIGHT / 2
        self.block.moveUp = False
        self.block.moveLeft = False
        self.block.moveDown = False
        self.block.moveRight = False
        self.bullets.clear()
        self.initialize_bullets()

    def update(self):
        """updates game state"""
        self.score.update()
        self.block.update()
        for bullet in self.bullets:
            bullet.update()

    def render(self):
        """draws display for game-loop"""
        self.score.draw()
        self.block.draw()
        for bullet in self.bullets:
            bullet.draw()

    def key_handle_down(self, key: int):
        """updates the velocity of block based on the key pressed down"""
        if key == pygame.K_w:
            self.block.moveUp = True
        elif key == pygame.K_a:
            self.block.moveLeft = True
        elif key == pygame.K_s:
            self.block.moveDown = True
        elif key == pygame.K_d:
            self.block.moveRight = True

    def key_handle_up(self, key: int):
        """for any direction, if the block has velocity in the same direction as its corresponding key, then
        the velocity in that direction is set back to 0"""
        if key == pygame.K_w and self.block.moveUp:
            self.block.moveUp = False
        elif key == pygame.K_a and self.block.moveLeft:
            self.block.moveLeft = False
        elif key == pygame.K_s and self.block.moveDown:
            self.block.moveDown = False
        elif key == pygame.K_d and self.block.moveRight:
            self.block.moveRight = False
