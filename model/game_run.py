import random as rand

import pygame
from pygame.surface import Surface

from model.block import Block
from model.bullet import Bullet
from model.score import Score


class GameRun:
    BULLET_VELOCITIES: list = list(range(-8, -5)) + list(range(5, 8))
    num_bullets: int = 3
    bullets: list
    display: Surface
    score: Score

    def __init__(self, display: Surface):
        self.display = display
        self.score = Score(display)
        self.bullets = [Bullet(display) for _ in range(self.num_bullets)]
        self.block = Block(display, (display.get_width() // 2 - Block.WIDTH // 2,
                                     display.get_height() // 2 - Block.HEIGHT // 2), self.bullets)

    def reset(self):
        """resets block to center position with 0 velocity and randomizes bullet movement fields"""
        self.score.current_score = 0
        self.block.rect.x = self.display.get_width() // 2 - self.block.WIDTH // 2
        self.block.rect.y = self.display.get_height() // 2 - self.block.HEIGHT // 2
        self.block.move_up = False
        self.block.move_left = False
        self.block.move_down = False
        self.block.move_right = False
        for bullet in self.bullets:
            bullet.randomize()

    def check_game_over(self):
        return self.block.check_collide_bullet()

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
            self.block.move_up = True
        elif key == pygame.K_a:
            self.block.move_left = True
        elif key == pygame.K_s:
            self.block.move_down = True
        elif key == pygame.K_d:
            self.block.move_right = True

    def key_handle_up(self, key: int):
        """for any direction, if the block has velocity in the same direction as its corresponding key, then
        the velocity in that direction is set back to 0"""
        if key == pygame.K_w and self.block.move_up:
            self.block.move_up = False
        elif key == pygame.K_a and self.block.move_left:
            self.block.move_left = False
        elif key == pygame.K_s and self.block.move_down:
            self.block.move_down = False
        elif key == pygame.K_d and self.block.move_right:
            self.block.move_right = False
