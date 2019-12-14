import pygame

from src.main.model.Block import *
from src.main.model.Bullet import Bullet
from src.main.ui.GameRun import GameRun
import random as rand

pygame.init()
pygame.display.set_caption('Blocky World Program')
clock = pygame.time.Clock()

width = 600
height = 400
display = pygame.display.set_mode((width, height))
fps = 100

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


def random_move(block: Block):
    choice = rand.choice([(0, 6), (6, 6), (6, 0), (6, -6), (0, -6), (-6, -6), (-6, 0), (-6, 6), (0, 0)])
    vx, vy = choice
    block.set_vx(vx)
    block.set_vy(vy)


def trial_game():
    block_width = 80
    block_height = 60
    block = Block(width / 2 - block_width / 2, height / 2 - block_height / 2, 0, 0,
                  block_width, block_height, black)
    bullets = [Bullet(display) for i in range(2)]
    game_run = GameRun(display, block, bullets)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        random_move(block)
        display.fill(white)
        if game_run.is_game_over():
            return pygame.time.get_ticks()
        game_run.draw_objects()
        game_run.update_game()
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    lot = []
    for i in range(10):
        time = trial_game()
        lot.append(time)
    mean = sum(lot) / len(lot)
    print(mean / 1000)
