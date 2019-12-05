import pygame

from src.main.model.Block import *

pygame.init()
pygame.display.set_caption('Blocky World Program')
clock = pygame.time.Clock()

width = 500
height = 500
block_width = 80
block_height = 60
fps = 100
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

block = Block(width / 2, height / 2, 0, 0, 50, 75, black)


# EFFECTS: updates the velocity of the block based on the key pressed down
def key_handle_down(b: Block, key: str):
    if key == pygame.K_w:
        b.set_vy(-6)
    elif key == pygame.K_s:
        b.set_vy(6)
    elif key == pygame.K_a:
        b.set_vx(-6)
    elif key == pygame.K_d:
        b.set_vx(6)


# EFFECTS: returns velocity to 0 when keys corresponding to a direction is let go
def key_handle_up(b: Block, key: str):
    if key == pygame.K_w or key == pygame.K_s:
        b.set_vy(0)
    elif key == pygame.K_a or key == pygame.K_d:
        b.set_vx(0)


if __name__ == '__main__':
    game_display = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key_handle_down(block, event.key)  # key handling
            if event.type == pygame.KEYUP:
                key_handle_up(block, event.key)  # key handling

        game_display.fill(white)
        block.update_block()  # update block
        pygame.draw.rect(game_display, block.colour,
                         (block.x, block.y, block.width, block.height), 0)  # render block
        pygame.display.update()
        clock.tick(fps)
