from math import radians, sin, cos
import pygame


class Boid2D:
    def __init__(self, top_left, width, height):
        self.x, self.y = top_left
        self.width = width
        self.height = height
        self.color = (0, 0, 255)
        self.nodes = [[self.x, self.y],
                      [self.x + width, self.y],
                      [self.x + width // 2, self.y + height]]
        self.center = [sum(n[0] for n in self.nodes) // 3, sum(n[1] for n in self.nodes) // 3]
        self.rotation = 0

    def draw(self, surface):
        pygame.draw.polygon(surface, self.color, self.nodes)

    def rotate(self, degrees):
        sin_theta = sin(radians(degrees))
        cos_theta = cos(radians(degrees))
        for node in self.nodes:
            x, y = node[0] - self.center[0], node[1] - self.center[1]
            node[0] = self.center[0] + (x * cos_theta - y * sin_theta)
            node[1] = self.center[1] + (y * cos_theta + x * sin_theta)
        self.rotation = (self.rotation + degrees) % 360

    def set_rotation(self, degrees):
        self.rotate(degrees % 360 - self.rotation)


