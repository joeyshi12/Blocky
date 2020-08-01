import os
import pygame


class Block:
    WIDTH: int = 50
    HEIGHT: int = 50
    SPEED: int = 5

    surface: pygame.Surface
    rect: pygame.Rect
    image: pygame.Surface
    bullets: list
    move_up: bool = False
    move_down: bool = False
    move_left: bool = False
    move_right: bool = False
    is_alive: bool = True

    def __init__(self, surface: pygame.Surface, pos: tuple, bullets: list=[], network=None):
        self.surface = surface
        self.rect = pygame.Rect(pos, (self.WIDTH, self.HEIGHT))
        dirname = os.path.dirname(__file__)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(dirname, "..", "data", "blocky.png")),
                                            (self.WIDTH, self.HEIGHT))
        self.bullets = bullets
        self.network = network

    def update(self):
        """updates block position"""
        if self.check_collision():
            self.is_alive = False
        if self.move_up:
            if self.rect.y > 0:
                self.rect.y -= self.SPEED
        if self.move_down:
            if self.rect.y + self.HEIGHT < self.surface.get_height():
                self.rect.y += self.SPEED
        if self.move_left:
            if self.rect.x > 0:
                self.rect.x -= self.SPEED
        if self.move_right:
            if self.rect.x + self.WIDTH < self.surface.get_width():
                self.rect.x += self.SPEED

    def check_collision(self):
        return self.check_collide_wall() or self.check_collide_bullet()

    def check_collide_wall(self):
        return self.rect.y <= 0 or self.rect.y + self.HEIGHT >= self.surface.get_height() or self.rect.x <= 0 or self.rect.x + self.WIDTH >= self.surface.get_width()

    def check_collide_bullet(self):
        for bullet in self.bullets:
            if self.rect.colliderect(bullet):
                return True
        return False

    def draw(self):
        """draws block on display"""
        self.surface.blit(self.image, self.rect.topleft)

    def get_data(self):
        inputs = [self.rect.centerx / self.surface.get_width(), self.rect.centery / self.surface.get_height()]
        for bullet in self.bullets:
            dx = self.rect.centerx - bullet.rect.centerx
            dy = self.rect.centery - bullet.rect.centery
            inputs.append((dx ** 2 + dy ** 2) / (self.surface.get_width() ** 2 + self.surface.get_height() ** 2))
            inputs.append(dx / self.surface.get_width())
            inputs.append(dy / self.surface.get_height())
            inputs.append(bullet.vx)
            inputs.append(bullet.vy)
        return inputs

    def predict(self):
        """make prediction from input data using self.network"""
        action = self.network.activate(self.get_data())
        i = action.index(max(action))

        if i == 0:
            self.move_up = False
            self.move_down = False
            self.move_left = False
            self.move_right = True
        elif i == 1:
            self.move_up = True
            self.move_down = False
            self.move_left = False
            self.move_right = True
        elif i == 2:
            self.move_up = True
            self.move_down = False
            self.move_left = False
            self.move_right = False
        elif i == 3:
            self.move_up = True
            self.move_down = False
            self.move_left = True
            self.move_right = False
        elif i == 4:
            self.move_up = False
            self.move_down = False
            self.move_left = True
            self.move_right = False
        elif i == 5:
            self.move_up = False
            self.move_down = True
            self.move_left = True
            self.move_right = False
        elif i == 6:
            self.move_up = False
            self.move_down = True
            self.move_left = False
            self.move_right = False
        else:
            self.move_up = False
            self.move_down = True
            self.move_left = False
            self.move_right = True
