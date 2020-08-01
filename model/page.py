import pygame
from pygame.surface import Surface

from model.button import Button


class Page:
    display: Surface

    def __init__(self, display: Surface, button_list=None):
        """Initializes background and buttonList. Background may be either a
        blank canvas or an image"""
        if button_list is None:
            button_list = []
        self.display = display
        self.button_list = button_list

    def on_click(self, pos: tuple) -> Button:
        """This method is called when the mouse is pressed down in an event
        loop. Check every button to see if “pos” is within them. If so, execute the
        button’s command through button.execute() and return that Button"""
        for button in self.button_list:
            if button.is_within(pos):
                button.execute()
                return button

    def create_button(self, identifier: str, pos: tuple, dimensions: tuple, text=None, font=None, command=None):
        """Creates a button and appends it to self.buttonList"""
        button = Button(identifier, pos, dimensions, text, font, command)
        self.button_list.append(button)

    def arrange_buttons(self, orientation: str, start_pos: tuple, padding: int):
        """Arranges all of the buttons in self.button_list to be separated lined
        up in either 'horizontal' or 'vertical' orientation starting at “start_pos”
        with “padding” amount of separation between these buttons"""
        if orientation == 'horizontal':
            self.orient_horizontal(padding, start_pos)
        elif orientation == 'vertical':
            self.orient_vertical(padding, start_pos)

    def orient_vertical(self, padding: int, start_pos: tuple):
        length = len(self.button_list)
        for i in range(length):
            button = self.button_list[i]
            new_pos = (start_pos[0], start_pos[1] + i * padding)
            self.button_list[i] = Button(button.identifier,
                                         new_pos,
                                         (button.rect.width, button.rect.height),
                                         button.command,
                                         button.text,
                                         button.font)

    def orient_horizontal(self, padding: int, start_pos: tuple):
        length = len(self.button_list)
        for i in range(length):
            button = self.button_list[i]
            new_pos = (start_pos[0] + i * padding, start_pos[1])
            self.button_list[i] = Button(button.identifier,
                                         new_pos,
                                         (button.rect.width, button.rect.height),
                                         button.command,
                                         button.text,
                                         button.font)

    def draw_buttons(self, display: Surface, mouse_pos: tuple, clicking: bool):
        """Draws the buttons in this Page’s buttonList"""
        for button in self.button_list:
            button.draw_button(display, mouse_pos, clicking)

    def page_loop(self, draw_fn):
        """Runs page loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    self.on_click(pygame.mouse.get_pos())
            self.display.fill((0, 0, 0))
            draw_fn()
            self.draw_buttons(self.display, pygame.mouse.get_pos(), pygame.mouse.get_pressed() == (1, 0, 0))
            pygame.display.update()
