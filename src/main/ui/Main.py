import pygame

from src.main.model.Block import *
from src.main.model.Bullet import Bullet
from src.main.model.Button import Button
from src.main.model.Page import Page
from src.main.ui.GameRun import GameRun
from src.main.ui.KeyHandling import key_handle_down, key_handle_up

pygame.init()
pygame.display.set_caption('Blocky World Program')
icon = pygame.image.load(r'C:\Users\j\Desktop\PycharmProjects\Blocky\src\main\data\chiken.jpg')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
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
    font = pygame.font.SysFont("freesansbold", 72)
    title = font.render("BLOCKY", True, red)
    start_button = Button("start_button", (0, 0), (100, 40), main, "Start",
                          pygame.font.Font("freesansbold.ttf", 12))
    info_button = Button("info_button", (0, 0), (100, 40), info_page, "Info",
                         pygame.font.Font("freesansbold.ttf", 12))
    button_list = [start_button, info_button]
    page = Page(display, button_list)
    page.arrange_buttons("vertical", (width / 2 - 50, height / 2 - 20), 100)

    def draw_fn():
        display.blit(title, (width / 2 - title.get_width() / 2, 50))
        page.draw_buttons(display, pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    while True:
        page_loop(draw_fn, page)


def info_page():
    image = pygame.image.load(r'C:\Users\j\Desktop\PycharmProjects\Blocky\src\main\data\control_info.jpg')
    image_width = int(width / 2)
    image_height = int(height / 2)
    image = pygame.transform.scale(image, (image_width, image_height))
    back_button = Button("back_button", (width / 2 - 50, height / 2 + 80), (100, 40), menu_page, "Back",
                         pygame.font.Font("freesansbold.ttf", 12))
    page = Page(display, [back_button])

    def draw_fn():
        display.blit(image, (width / 2 - image_width / 2, 0))
        page.draw_buttons(display, pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    while True:
        page_loop(draw_fn, page)


def page_loop(draw_fn, page):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            page.on_click(pygame.mouse.get_pos())
    display.fill(white)
    draw_fn()
    pygame.display.update()
    clock.tick(fps)


def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.circle(display, black, (bullet.x, bullet.y), bullet.radius)
        bullet.update()


def main():
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
            if event.type == pygame.KEYDOWN:
                key_handle_down(block, event.key)  # key handling
            if event.type == pygame.KEYUP:
                key_handle_up(block, event.key)  # key handling

        display.fill(white)
        if game_run.is_game_over():
            menu_page()
        game_run.draw_objects()
        game_run.update_game()
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    menu_page()
