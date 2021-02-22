from math import radians, sin, cos
import pygame


class Boid2D:
    def __init__(self, top_left, size):
        self.x, self.y = top_left
        self.size = self.width, self.height = size
        self.color = (0, 0, 255)
        self.nodes = [[self.x, self.y],
                      [self.x, self.y + self.height],
                      [self.x + self.width, self.y + self.height // 2]]
        self.center = [sum(n[0] for n in self.nodes) // 3, sum(n[1] for n in self.nodes) // 3]
        self.rotation = 0
        self.velocity = 0
        self.settings = None

    def update(self, screen, delta_time, settings):
        self.settings = settings
        self._update_center()
        self.draw(screen)

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

    def _update_center(self):
        self.center = [sum(n[0] for n in self.nodes) // 3, sum(n[1] for n in self.nodes) // 3]

    def get_forward_vector(self):
        unit_x = self.velocity * cos(radians(self.rotation))
        unit_y = self.velocity * sin(radians(self.rotation))
        return unit_x, unit_y

    def move_forward(self, delta_t):
        unit_x, unit_y = self.get_forward_vector()
        for node in self.nodes:
            node[0] += unit_x * delta_t
            node[1] += unit_y * delta_t
