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

RECTANGLES_NUMBER = 8
RECTANGLES = {}

BRICK_COLOR = (0, 255, 0)


class PolyBricks:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Polybricks")
        self.selected_rectangle_id = 0

        if pygame.font:
            self.font = pygame.font.Font(None, 30)
        else:
            self.font = None

        self.init_game()

    def init_game(self):
        self.lives = 3
        self.score = 0
        self.old_keys = {}

    def show_stats(self):
        if self.font:
            font_surface = self.font.render(
                "SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False, TEXT_FILL)
            self.screen.blit(font_surface, (400, 5))

    def rotate_point(self, landmark, point, orientation):
        orientation *= math.pi/180.0 # Convert to radian
        return ((point[0] * math.cos(orientation) - point[1] * math.sin(orientation))+landmark[0],
                (point[0] * math.sin(orientation) + point[1] * math.cos(orientation))+landmark[1])

    def get_rectangle(self, x, y, width, length, orientation):
        pointlist = [(x,y)]
        pointlist.append(self.rotate_point((x,y), (width, 0), orientation))
        pointlist.append(self.rotate_point((x, y),  (width, length), orientation))
        pointlist.append(self.rotate_point((x,y), (0, length), orientation))
        return pointlist

    def show_rectangles(self):
        if RECTANGLES:
            pygame.draw.polygon(self.screen, BRICK_COLOR,
                                RECTANGLES[self.selected_rectangle_id], 0)
        else:
            self.init_rectangles()
            
    def init_rectangles(self):
        center = [int(x/2) for x in SCREEN_SIZE]
        radius = SCREEN_SIZE[1]/4
        side = 2*radius*math.sin(math.pi/RECTANGLES_NUMBER)
        thickness = 50
        angle_gain = 360/RECTANGLES_NUMBER

        angle = 0
        extrem = int(center[0]-side/2), int(center[1] - math.sqrt(radius**2 - (side/2)**2))
        for i in range(0, RECTANGLES_NUMBER):
            RECTANGLES[i] = self.get_rectangle(
                extrem[0], extrem[1], side, -thickness, angle)
            extrem = [int(x) for x in self.rotate_point(extrem, (side, 0), angle)]
            angle += angle_gain
            
        self.show_rectangles()
        
    def check_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and not self.old_keys[pygame.K_LEFT]:
            self.selected_rectangle_id = (self.selected_rectangle_id-1)%RECTANGLES_NUMBER

        if keys[pygame.K_RIGHT] and not self.old_keys[pygame.K_RIGHT]:
            self.selected_rectangle_id = (self.selected_rectangle_id+1) % RECTANGLES_NUMBER

        self.old_keys = keys
        #if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:

        #elif keys[pygame.K_RETURN] and (self.state == STATE_GAME_OVER or self.state == STATE_WON):
            #self.init_game()

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.check_input()
            self.screen.fill(BACKGROUND)
            self.show_rectangles()
            self.show_stats()
            pygame.display.flip()


if __name__ == "__main__":
    RECTANGLES_NUMBER = 8  # int(input("Number of rectangles:"))
    PolyBricks().run()
