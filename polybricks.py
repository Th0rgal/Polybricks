import sys
import pygame
import math
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

    def rotate_point(self, landmark, point, orientation):
        orientation *= math.pi/180.0 # Convert to radian
        return ((point[0] * math.cos(orientation) - point[1] * math.sin(orientation))+landmark[0],
                (point[0] * math.sin(orientation) + point[1] * math.cos(orientation))+landmark[1])

    def draw_rectangle(self, x, y, width, length, orientation, color):
        pointlist = [(x,y)]
        pointlist.append(self.rotate_point((x,y), (width, 0), orientation))
        pointlist.append(self.rotate_point((x, y),  (width, length), orientation))
        pointlist.append(self.rotate_point((x,y), (0, length), orientation))
        pygame.draw.polygon(self.screen, color, pointlist, 0)


    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.screen.fill(BACKGROUND)
            self.draw_rectangle(
                SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, 150, 50, 45, BRICK_COLOR)
            self.draw_rectangle(
                SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, 150, 50, 0, TEXT_FILL)
            self.show_stats()
            pygame.display.flip()


if __name__ == "__main__":

    rectangles_number = 8  # int(input("Number of rectangles:"))

    PolyBricks().run()
