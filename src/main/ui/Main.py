import pygame
from pygame.surface import Surface

from src.main.model.Block import *
from src.main.model.Bullet import Bullet
from src.main.model.Button import Button
from src.main.model.Page import Page
from src.main.ui.KeyHandling import key_handle_down, key_handle_up

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


def menu_page():
    start_button = Button("start_button", (0, 0), (100, 40), main_page, "Start",
                          pygame.font.Font("freesansbold.ttf", 12))
    info_button = Button("info_button", (0, 0), (100, 40), info_page, "Info",
                         pygame.font.Font("freesansbold.ttf", 12))
    button_list = [start_button, info_button]
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
        clock.tick(fps)


def info_page():
    image = pygame.image.load(r'C:\Users\j\Desktop\PycharmProjects\Blocky\src\main\data\control_info.jpg')
    image_width = int(width / 2)
    image_height = int(height / 2)
    image = pygame.transform.scale(image, (image_width, image_height))
    back_button = Button("back_button", (width / 2 - 50, height / 2 + 80), (100, 40), menu_page, "Back",
                         pygame.font.Font("freesansbold.ttf", 12))
    page = Page(display, [back_button])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                page.on_click(pygame.mouse.get_pos())

        display.fill(white)
        display.blit(image, (width / 2 - image_width / 2, 0))
        page.draw_buttons(display, pygame.mouse.get_pos(), pygame.mouse.get_pressed())
        pygame.display.update()
        clock.tick(fps)


def is_game_over(display: Surface, block: Block, bullets: list) -> bool:
    if block.x < 0 or block.x + block.width > display.get_width() or \
            block.y < 0 or block.y + block.height > display.get_height():
        return True
    for bullet in bullets:
        if block.x <= bullet.x <= block.x + block.width and block.y <= bullet.y <= block.y + block.height:
            return True
    return False


def main_page():
    block_width = 80
    block_height = 60
    block = Block(width / 2 - block_width / 2, height / 2 - block_height / 2, 0, 0, block_width, block_height, black)
    bullet1 = Bullet(display)
    bullet2 = Bullet(display)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                key_handle_down(block, event.key)  # key handling
            if event.type == pygame.KEYUP:
                key_handle_up(block, event.key)  # key handling

        if is_game_over(display, block, [bullet1, bullet2]):
            menu_page()
        display.fill(white)
        block.update_block()  # update block
        pygame.draw.rect(display, block.colour,
                         (block.x, block.y, block.width, block.height), 0)  # render block
        pygame.draw.circle(display, black, (bullet1.x, bullet1.y), bullet1.radius)
        bullet1.update_bullet()
        pygame.draw.circle(display, black, (bullet2.x, bullet2.y), bullet2.radius)
        bullet2.update_bullet()
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    menu_page()
