import pygame
import os
import math
import sys
import random
import neat
from Block import Block
from Bullet import Bullet

display_width = 800
display_height = 500
generation = 0

def random_bullets(display, num_bullets):
    """creates num_bullets of bullets with random movement fields"""
    bullets = list()
    bullet_velocities = [-7, 7]
    for i in range(num_bullets):
        bullet_x = random.choice([random.randint(0, display.get_width() // 4), random.randint(3 * display.get_width() // 4, display.get_width())])
        bullet_y = random.choice([random.randint(0, display.get_height() // 4), random.randint(3 * display.get_height() // 4, display.get_height())])
        bullet_dy = random.choice(bullet_velocities)
        bullet_dx = random.choice(bullet_velocities)
        bullet = Bullet(display, (bullet_x, bullet_y), (bullet_dx, bullet_dy))
        bullets.append(bullet)
    return bullets


def run_genome(genomes, config):
    # Init game
    pygame.init()
    pygame.display.set_caption('Blocky World Program')
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((display_width, display_height))
    bullets = random_bullets(display, 3)
    generation_font = pygame.font.SysFont("Arial", 70)
    font = pygame.font.SysFont("Arial", 30)

    # Init NEAT
    nets = list()
    blocks = list()

    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0

        # Init my cars
        blocks.append(Block(display, (display_width // 2, display_height // 2), bullets))

    # Main loop
    global generation
    generation += 1
    while True:
        display.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Input my data and get result from network
        for index, block in enumerate(blocks):
            output = nets[index].activate(block.getData())
            i = output.index(max(output))
            if i == 0:
                block.moveUp = True
                block.moveDown = False
                block.moveLeft = False
                block.moveRight = False
            if i == 1:
                block.moveUp = False
                block.moveDown = True
                block.moveLeft = False
                block.moveRight = False
            if i == 2:
                block.moveUp = False
                block.moveDown = False
                block.moveLeft = True
                block.moveRight = False
            if i == 3:
                block.moveUp = False
                block.moveDown = False
                block.moveLeft = False
                block.moveRight = True

        # Update car and fitness
        remain_blocks = 0
        for i, block in enumerate(blocks):
            if block.isAlive:
                remain_blocks += 1
                block.update()
                genomes[i][1].fitness += block.timeAlive

        for bullet in bullets:
            bullet.update()
            bullet.draw()

        # check
        if remain_blocks == 0:
            break

        # Drawing
        for block in blocks:
            if block.isAlive:
                block.draw()

        text = generation_font.render("Generation : " + str(generation), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (display_width/2, 100)
        display.blit(text, text_rect)

        text = font.render("remaining blocks : " + str(remain_blocks), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (display_width/2, 200)
        display.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(120)


if __name__ == "__main__":
    # Set configuration file
    config_path = "./config-feedforward.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(run_genome, 1000)
