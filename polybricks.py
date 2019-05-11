import sys
import pygame
import os

SCREEN_SIZE = 1040, 768

BACKGROUND = (22, 31, 40)
TEXT_FILL = (255, 255, 255)

STATE_PAUSED = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

RECTANGLES = []

BRICK_COLOR = (0, 255, 0)


class PolyBricks:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Polybricks")

        if pygame.font:
            self.font = pygame.font.Font(None, 30)
        else:
            self.font = None

        self.init_game()

    def init_game(self):
        self.lives = 3
        self.score = 0

    def show_stats(self):
        if self.font:
            font_surface = self.font.render(
                "SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, TEXT_FILL)
            self.screen.blit(font_surface, (400, 5))

    def draw_rectangle(self, x, y, width, length, orientation):
        a = (x, y)

    def show_rectangles(self):
        self.draw_rectangle()

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.screen.fill(BACKGROUND)
            self.show_rectangles()
            self.show_stats()
            pygame.display.flip()


if __name__ == "__main__":

    rectangles_number = 8  # int(input("Number of rectangles:"))

    PolyBricks().run()
