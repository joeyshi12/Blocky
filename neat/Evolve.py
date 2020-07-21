import pickle
import random
import sys

import neat
import visualize
from joblib import dump
import pygame
from Block import Block
from Bullet import Bullet

surface_width = 800
surface_height = 500
generation = 0
num_bullets = 3


def eval_genomes(genomes, config):
    # Init game
    pygame.init()
    pygame.display.set_caption('Blocky World Program')
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((surface_width, surface_height))
    bullets = [Bullet(surface) for _ in range(3)]
    generation_font = pygame.font.SysFont("Arial", 70)
    font = pygame.font.SysFont("Arial", 30)

    # Init NEAT
    blocks = list()

    for id, g in genomes:
        network = neat.nn.FeedForwardNetwork.create(g, config)
        g.fitness = 0

        # Init my cars
        blocks.append(Block(surface, (surface_width // 2, surface_height // 2), bullets, network=network))

    # Main loop
    global generation
    generation += 1
    while True:
        surface.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Each block predicts next move
        for block in blocks:
            block.predict()

        # Update block and fitness
        remain_blocks = 0
        for i, block in enumerate(blocks):
            if block.is_alive:
                remain_blocks += 1
                block.update()
                genomes[i][1].fitness += 0.1
                if block.check_collide_wall():
                    genomes[i][1].fitness -= 1

        for bullet in bullets:
            bullet.update()
            bullet.draw()

        # check
        if remain_blocks == 0:
            break

        # Drawing
        for block in blocks:
            if block.is_alive:
                block.draw()

        text = generation_font.render("Generation : " + str(generation), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (surface_width / 2, 100)
        surface.blit(text, text_rect)

        text = font.render("remaining blocks : " + str(remain_blocks), True, (255, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (surface_width / 2, 200)
        surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(0)


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
    winner = p.run(eval_genomes, 100)
    with open('winner.pkl', 'wb') as output:
        pickle.dump(winner, output, 1)

    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)



