import pygame
from pygame.surface import Surface

from src.main.model.Block import Block


class GameRun:
    def __init__(self, display: Surface, block: Block, bullets: list):
        self.display = display
        self.block = block
        self.bullets = bullets

    def collide_wall(self) -> bool:
        return self.block.x < 0 or self.block.x + self.block.width > self.display.get_width() or \
               self.block.y < 0 or self.block.y + self.block.height > self.display.get_height()

    def collide_bullet(self) -> bool:
        for bullet in self.bullets:
            if bullet.block.x <= bullet.x <= bullet.block.x + bullet.block.width and \
                    bullet.block.y <= bullet.y <= bullet.block.y + bullet.block.height:
                return True
        return False

    def is_game_over(self) -> bool:
        return self.collide_wall() or self.collide_bullet()

    def update_game(self):
        self.block.update_block()
        for bullet in self.bullets:
            bullet.update_bullet()

    def draw_objects(self):
        pygame.draw.rect(self.display, self.block.colour,
                         (self.block.x, self.block.y, self.block.width, self.block.height), 0)  # render block
        for bullet in self.bullets:
            pygame.draw.circle(self.display, (0, 0, 0), (bullet.x, bullet.y), bullet.radius)
            bullet.update_bullet()
