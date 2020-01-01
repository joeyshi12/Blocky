import pygame
from pygame.font import Font
from pygame.surface import Surface


class Score:
    FONT_COLOUR: tuple = (255, 0, 0)
    FONT_SIZE: int = 20

    current_score: int = 0
    high_score: int
    font: Font

    def __init__(self, display: Surface):
        self.display = display
        self.load()
        self.font = pygame.font.SysFont("lucidaconsole", self.FONT_SIZE)

    def save(self):
        """writes high score to high_score.txt"""
        file = open("data/high_score.txt", 'w')
        file.write(str(self.high_score))
        file.close()

    def load(self):
        """sets high_score to int inside of high_score.txt"""
        file = open("data/high_score.txt", 'r')
        self.high_score = int(file.read())
        file.close()

    def update(self):
        """updates current_score and high_score for next game frame"""
        self.current_score += 1
        self.high_score = max([self.current_score, self.high_score])

    def draw(self):
        """draws score board on display"""
        high_score_render = self.font.render("High Score: " + str(self.high_score), True, self.FONT_COLOUR)
        score_render = self.font.render("Score: " + str(self.current_score), True, self.FONT_COLOUR)
        self.display.blit(high_score_render, (10, 10))
        self.display.blit(score_render, (10, 10 + self.FONT_SIZE))
