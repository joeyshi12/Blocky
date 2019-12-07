import pygame

from src.main.model.Block import *
from src.main.model.Button import Button
from src.main.model.Page import Page
from src.main.ui.KeyHandling import key_handle_down, key_handle_up

pygame.init()
pygame.display.set_caption('Blocky World Program')
clock = pygame.time.Clock()

width = 600
height = 400
block_width = 80
block_height = 60
fps = 100
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
block = Block(width / 2 - block_width / 2, height / 2 - block_height / 2, 0, 0, block_height, block_width, black)


def menu_page():
    display = pygame.display.set_mode((width, height))
    start_button = Button("start_button", (0, 0), (100, 40), main_page, "Start",
                          pygame.font.Font("freesansbold.ttf", 12))
    settings_button = Button("settings_button", (0, 0), (100, 40), main_page, "Settings",
                             pygame.font.Font("freesansbold.ttf", 12))
    button_list = [start_button, settings_button]
    page = Page(display, button_list)
    page.arrange_buttons("vertical", (width / 2 - 50, height / 2 - 20), 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                page.on_click(pygame.mouse.get_pos())

        display.fill(white)
        page.draw_buttons(display, pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        pygame.display.update()
        clock.tick(200)


def main_page():
    display = pygame.display.set_mode((width, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key_handle_down(block, event.key)  # key handling
            if event.type == pygame.KEYUP:
                key_handle_up(block, event.key)  # key handling

        display.fill(white)
        block.update_block()  # update block
        pygame.draw.rect(display, block.colour,
                         (block.x, block.y, block.width, block.height), 0)  # render block
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    menu_page()
