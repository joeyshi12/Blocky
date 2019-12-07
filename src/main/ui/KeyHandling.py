import pygame

from src.main.model.Block import Block


def key_handle_down(b: Block, key: str):
    """updates the velocity of the block based on the key pressed down"""
    if key == pygame.K_w:
        b.set_vy(-6)
    elif key == pygame.K_s:
        b.set_vy(6)
    elif key == pygame.K_a:
        b.set_vx(-6)
    elif key == pygame.K_d:
        b.set_vx(6)


def key_handle_up(b: Block, key: str):
    """returns velocity to 0 when keys corresponding to a direction is let go"""
    if key == pygame.K_w or key == pygame.K_s:
        b.set_vy(0)
    elif key == pygame.K_a or key == pygame.K_d:
        b.set_vx(0)