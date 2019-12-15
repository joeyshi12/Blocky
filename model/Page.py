from pygame.surface import Surface

from model.Button import Button


class Page:
    def __init__(self, background: Surface, button_list=None):
        """Initializes background and buttonList. Background may be either a
blank canvas or an image"""
        if button_list is None:
            button_list = []
        self.background = background
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
with “padding” amount of separation between these buttons. For each Button in
self.buttonList, you’ll likely have to access and modify its buttonRect
attributes such as topleft. See documentation on Rect attributes for more
information"""
        if orientation == 'horizontal':
            self.orient_horizontal(padding, start_pos)
        elif orientation == 'vertical':
            self.orient_vertical(padding, start_pos)

    def orient_vertical(self, padding, start_pos):
        length = len(self.button_list)
        for i in range(length):
            button = self.button_list[i]
            new_pos = (start_pos[0], start_pos[1] + i * padding)
            self.button_list[i] = Button(button.identifier,
                                         new_pos,
                                         (button.button_rect.width, button.button_rect.height),
                                         button.command,
                                         button.text,
                                         button.font)

    def orient_horizontal(self, padding, start_pos):
        length = len(self.button_list)
        for i in range(length):
            button = self.button_list[i]
            new_pos = (start_pos[0] + i * padding, start_pos[1])
            self.button_list[i] = Button(button.identifier,
                                         new_pos,
                                         (button.button_rect.width, button.button_rect.height),
                                         button.command,
                                         button.text,
                                         button.font)

    def draw_buttons(self, display: Surface, mouse_pos: tuple, clicking: bool):
        """Draws the buttons in this Page’s buttonList"""
        for button in self.button_list:
            button.draw_button(display, mouse_pos, clicking)

    def create_display(self, main_display: Surface):
        """ This will be page’s event and draw loop. First, draw self.background
onto main_display through the blit() method. For now, we won’t handle any
keyboard inputs so the only input we will check are mouse button presses."""
        pass
