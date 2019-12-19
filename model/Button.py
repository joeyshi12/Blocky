import pygame
from pygame import Surface, Rect


class Button:
    def __init__(self, identifier: str, pos: tuple, dimensions: tuple, command=None, text=None, font=None):
        self.identifier = identifier
        self.button_rect = pygame.Rect(pos, dimensions)
        self.command = command
        self.text = text
        self.font = font

    def execute(self):
        """executes self.command()"""
        self.command()

    def render_text(self) -> (Surface, Rect):
        """returns a rendered text with proper font in black colour and
a rectangle in which the rendered text will be placed in"""
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def draw_text(self, display: Surface):
        """draws rendered text in the center of rectangle"""
        text_surf, text_rect = self.render_text()
        center_x = (self.button_rect.left + (self.button_rect.width / 2))
        center_y = (self.button_rect.top + (self.button_rect.height / 2))
        text_rect.center = (center_x, center_y)
        display.blit(text_surf, text_rect)

    def draw_state(self, display: Surface, state: str):
        """draws rectangle with a colour depending on the given state"""
        if state == 'regular':
            pygame.draw.rect(display, (255, 0, 0), self.button_rect)
        elif state == 'within':
            pygame.draw.rect(display, (0, 255, 0), self.button_rect)
        elif state == 'clicking':
            pygame.draw.rect(display, (0, 0, 255), self.button_rect)

    def is_within(self, mouse_pos: tuple) -> bool:
        """returns true if mouse is inside rectangle; false otherwise"""
        is_within_x = (self.button_rect.left < mouse_pos[0] < self.button_rect.left + self.button_rect.width)
        is_within_y = (self.button_rect.top < mouse_pos[1] < self.button_rect.top + self.button_rect.height)
        return is_within_x and is_within_y

    def draw_button(self, display: Surface, mouse_pos: tuple, clicking: bool):
        """execute draw_text on display if text exists and draw_state on display
with state given by:
is_within and clicking     -> 'clicking'
is_within and not clicking -> 'within'
not is_within              -> 'regular'"""
        if (self.text is not None) and (self.font is not None):
            if self.is_within(mouse_pos):
                if clicking:
                    self.draw_state(display, 'clicking')
                    self.draw_text(display)
                else:
                    self.draw_state(display, 'within')
                    self.draw_text(display)
            else:
                self.draw_state(display, 'regular')
                self.draw_text(display)
        else:
            if self.is_within(mouse_pos):
                if clicking:
                    self.draw_state(display, 'clicking')
                else:
                    self.draw_state(display, 'within')
            else:
                self.draw_state(display, 'regular')
