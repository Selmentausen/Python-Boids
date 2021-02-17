import math
import pygame


class Boid2D:
    def __init__(self, top_left, width, height):
        self.x, self.y = top_left
        self.width = width
        self.height = height
        self.color = (0, 0, 255)
        self.nodes = ((self.x, self.y),
                      (self.x + width, self.y),
                      (self.x + width // 2, self.y + height))

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.nodes)

    def rotate_x(self):
        pass

    def rotate_y(self):
        pass
