import pickle
import sys

import neat
import visualize
import pygame
from Block import Block
from Bullet import Bullet

surface_width = 800
surface_height = 500
num_bullets = 3


def main():
    pygame.init()
    pygame.display.set_caption('Test')
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((surface_width, surface_height))
    bullets = [Bullet(surface) for _ in range(3)]
    score = 0
    score_font = pygame.font.SysFont("Arial", 30)
    block = Block(surface, (surface_width // 2, surface_height // 2), bullets)
    while True:
        surface.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    block.move_up = True
                elif event.key == pygame.K_s:
                    block.move_down = True
                elif event.key == pygame.K_a:
                    block.move_left = True
                elif event.key == pygame.K_d:
                    block.move_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    block.move_up = False
                elif event.key == pygame.K_s:
                    block.move_down = False
                elif event.key == pygame.K_a:
                    block.move_left = False
                elif event.key == pygame.K_d:
                    block.move_right = False

        if block.is_alive:
            block.update()
            block.draw()
            score += 0.1

        for bullet in bullets:
            bullet.update()
            bullet.draw()

        if not block.is_alive:
            print(score)
            break

        text = score_font.render("Score: " + str(round(score)), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (surface_width / 2, 100)
        surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(200)


if __name__ == "__main__":
    while True:
        main()