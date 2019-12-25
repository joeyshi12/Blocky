import pygame

from model.Button import Button
from model.GameRun import GameRun
from model.Page import Page

pygame.init()
pygame.display.set_caption('Blocky World Program')
icon = pygame.image.load('data/chiken.jpg')
icon = pygame.transform.scale(icon, (32, 32))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
display_width = 800
display_height = 500
display = pygame.display.set_mode((display_width, display_height))

red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)


def menu():
    def draw_fn():
        display.blit(title, (int(display_width / 2 - title.get_width() / 2), 100))

    menu_page.page_loop(draw_fn)


def info_page():
    def draw_fn():
        display.blit(image, (display_width / 2 - image_width / 2, 0))
    info_page.page_loop(draw_fn)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_run.key_handle_down(event.key)
            if event.type == pygame.KEYUP:
                game_run.key_handle_up(event.key)
        display.fill(white)
        if game_run.is_game_over():
            game_run.reset()
            menu()
        game_run.draw()
        game_run.update_game()
        pygame.display.update()
        clock.tick(100)


if __name__ == '__main__':
    # Menu Components
    title_font = pygame.font.SysFont("freesansbold", 72)
    title = title_font.render("BLOCKY", True, red)
    start_button = Button("start_button", (0, 0), (100, 40), main, "Start",
                          pygame.font.Font("freesansbold.ttf", 12))
    info_button = Button("info_button", (0, 0), (100, 40), info_page, "Info",
                         pygame.font.Font("freesansbold.ttf", 12))
    button_list = [start_button, info_button]
    menu_page = Page(display, button_list)
    menu_page.arrange_buttons("vertical", (display_width / 2 - 50, display_height / 2 - 20), 100)

    # Info Components
    image = pygame.image.load('data/control_info.jpg')
    image_width = int(display_width / 2)
    image_height = int(display_height / 2)
    image = pygame.transform.scale(image, (image_width, image_height))
    back_button = Button("back_button", (display_width / 2 - 50, display_height / 2 + 80), (100, 40), menu_page, "Back",
                         pygame.font.Font("freesansbold.ttf", 12))
    info_page = Page(display, [back_button])

    # Run Game
    game_run = GameRun(display)
    menu()
