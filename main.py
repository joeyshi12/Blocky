import pickle

import neat
import pygame

from model.button import Button
from model.game_run import GameRun
from model.page import Page
import random as rand
import os

pygame.init()
pygame.display.set_caption('Blocky World Program')
icon = pygame.image.load('data/chiken.jpg')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
display_width = 700
display_height = 500
display = pygame.display.set_mode((display_width, display_height))

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


def menu():
    title_x = int(display_width / 2 - title.get_width() / 2)
    title_y = int(display_height / 5)

    def draw_fn():
        display.blit(title, (title_x, title_y))

    menu_page.page_loop(draw_fn)


def info_page():
    info_image_x = int(display_width / 2 - info_image.get_width() / 2)
    info_image_y = int(info_image.get_height() / 5)

    def draw_fn():
        display.blit(info_image, (info_image_x, info_image_y))

    info_page.page_loop(draw_fn)


def test_ai():
    config_path = "./neat/config-feedforward.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    with open('./neat/winner.pkl', 'rb') as f:
        c = pickle.load(f)
    network = neat.nn.FeedForwardNetwork.create(c, config)
    game_run.block.network = network
    game_run.score.start_timer()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if game_run.block.check_collide_bullet():
            game_run.reset()
            menu()
        display.fill((0, 0, 0))
        game_run.render()
        game_run.block.predict()
        game_run.update()
        pygame.display.update()
        clock.tick(120)


def main():
    game_run.score.start_timer()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_run.key_handle_down(event.key)
            if event.type == pygame.KEYUP:
                game_run.key_handle_up(event.key)
        if game_run.check_game_over():
            game_run.reset()
            menu()
        display.fill((0, 0, 0))
        game_run.render()
        game_run.update()
        pygame.display.update()
        clock.tick(120)


# Menu Components
button_dimensions = (100, 40)
font_style = "lucidaconsole"
title_font = pygame.font.SysFont(font_style, 72)
title = title_font.render("BLOCKY", True, (255, 0, 0))
start_button = Button("start_button", (0, 0), button_dimensions, main, "Start",
                      pygame.font.SysFont(font_style, 12))
run_ai_button = Button("run_ai_button", (0, 0), button_dimensions, test_ai, "Run A.I.",
                       pygame.font.SysFont(font_style, 12))
info_button = Button("info_button", (0, 0), button_dimensions, info_page, "Info",
                     pygame.font.SysFont(font_style, 12))
button_list = [start_button, run_ai_button, info_button]
menu_page = Page(display, button_list)
menu_page.arrange_buttons("vertical", (display_width // 2 - button_dimensions[0] // 2,
                                       display_height // 2 - button_dimensions[1] // 2), 60)


# Info Components
info_image = pygame.image.load('data/control_info.jpg')
info_image = pygame.transform.scale(info_image, (display_width // 2, display_height // 2))
back_button = Button("back_button", ((display_width - button_dimensions[0]) / 2, display_height / 2 + 100),
                     button_dimensions, menu, "Back", pygame.font.SysFont(font_style, 12))
info_page = Page(display, [back_button])


if __name__ == '__main__':
    game_run = GameRun(display)
    menu()
