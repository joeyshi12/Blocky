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
    title_x = int(display_width / 2 - title.get_width() / 2)
    title_y = int(display_height / 5)

    def draw_fn():
        display.blit(title, (title_x, title_y))
    menu_page.page_loop(draw_fn)


def info_page():
    info_image_x = int(display_width / 2 - info_image_width / 2)
    info_image_y = int(info_image_height / 5)

    def draw_fn():
        display.blit(info_image, (info_image_x, info_image_y))
    info_page.page_loop(draw_fn)


def save(ticks: int):
    file = open("data/high_score.txt", 'w')
    file.write(str(ticks))
    file.close()


def load() -> int:
    file = open("data/high_score.txt", 'r')
    high_score = int(file.read())
    file.close()
    return high_score


def main():
    ticks = 0
    previous_high_score = load()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                game_run.key_handle_down(event.key)
            if event.type == pygame.KEYUP:
                game_run.key_handle_up(event.key)
        display.fill(black)
        if game_run.is_game_over():
            save(max(ticks, load()))
            game_run.reset()
            menu()
        game_run.draw()
        high_score_render = high_score_font.render("High Score: " + str(max(previous_high_score, ticks)), True, red)
        score_render = score_font.render("Score: " + str(ticks), True, red)
        display.blit(high_score_render, (10, 10))
        display.blit(score_render, (10, 30))
        game_run.update_game()
        pygame.display.update()
        ticks += 1
        clock.tick(100)


# Menu Components
button_dimensions = (100, 40)
font_style = "lucidaconsole"
title_font = pygame.font.SysFont(font_style, 72)
title = title_font.render("BLOCKY", True, red)
start_button = Button("start_button", (0, 0), button_dimensions, main, "Start",
                      pygame.font.SysFont(font_style, 12))
info_button = Button("info_button", (0, 0), button_dimensions, info_page, "Settings",
                     pygame.font.SysFont(font_style, 12))
button_list = [start_button, info_button]
menu_page = Page(display, button_list)
menu_page.arrange_buttons("vertical", (display_width / 2 - 50, display_height / 2 - 20), 100)

# Info Components
info_image = pygame.image.load('data/control_info.jpg')
info_image_width = int(display_width / 2)
info_image_height = int(display_height / 2)
info_image = pygame.transform.scale(info_image, (info_image_width, info_image_height))
back_button = Button("back_button", (display_width / 2 - 50, display_height / 2 + 80),
                     button_dimensions, menu, "Back", pygame.font.SysFont(font_style, 12))
info_page = Page(display, [back_button])

# Score Display
high_score_font = pygame.font.SysFont(font_style, 20)
score_font = pygame.font.SysFont(font_style, 20)

if __name__ == '__main__':
    game_run = GameRun(display)
    menu()
