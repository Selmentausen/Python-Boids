import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True


class Shape:
    def __init__(self, coord, dimensions, node_color=(0, 0, 255), edge_color=(0, 255, 0), node_size=10):
        self.coord = coord
        self.dimensions = dimensions
        self.nodes = []
        self.edges = []
        self.node_color = node_color
        self.edge_color = edge_color
        self.node_size = node_size
        self.center = coord

    def draw(self, surface):
        for edge in self.edges:
            start_node, end_node = self.nodes[edge[0]], self.nodes[edge[1]]
            pygame.draw.line(surface, self.edge_color,
                             (start_node[0] + self.node_size // 2, start_node[1] + self.node_size // 2),
                             (end_node[0] + self.node_size // 2, end_node[1] + self.node_size // 2))
        for node in self.nodes:
            pygame.draw.ellipse(surface, self.node_color, (node[0], node[1], self.node_size, self.node_size))


class Pyramid(Shape):
    def __init__(self, coord, dimensions, node_color=(0, 0, 255), edge_color=(0, 255, 0), node_size=10):
        super(Pyramid, self).__init__(coord, dimensions, node_color, edge_color, node_size)
        x, y, z = self.coord
        w, h, d = self.dimensions
        self.nodes = [
            [x, y, z],
            [x + w, y, z],
            [x, y + h, z],
            [x + w, y + h, z],
            [x + w // 2, y + h // 2, z + d]
        ]
        self.edges = [
            [0, 1],
            [0, 2],
            [1, 3],
            [2, 3],
            [0, 4],
            [1, 4],
            [2, 4],
            [3, 4]
        ]
        self.center = (x + w // 2, y + h // 2, z + d // 2)


class Cuboid(Shape):
    def __init__(self, coord, dimensions, node_color=(0, 0, 255), edge_color=(0, 255, 0), node_size=10):
        super(Cuboid, self).__init__(coord, dimensions, node_color, edge_color, node_size)
        x, y, z = self.coord
        w, h, d = self.dimensions
        self.nodes = [
            [x, y, z],
            [x, y, z + d],
            [x, y + h, z],
            [x, y + h, z + d],
            [x + w, y, z],
            [x + w, y, z + d],
            [x + w, y + h, z],
            [x + w, y + h, z + d],
        ]
        self.edges = [
            [0, 1], [1, 3], [3, 2], [2, 0],
            [4, 5], [5, 7], [7, 6], [6, 4],
            [0, 4], [1, 5], [2, 6], [3, 7],
        ]
        self.center = (x + w // 2, y + h // 2, z + d // 2)


def rotate_z_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        x, y = node[0] - rotation_center[0], node[1] - rotation_center[1]
        node[0] = rotation_center[0] + (x * cos_theta - y * sin_theta)
        node[1] = rotation_center[1] + (y * cos_theta + x * sin_theta)


def rotate_x_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        y, z = node[1] - rotation_center[1], node[2] - rotation_center[2]
        node[1] = rotation_center[1] + (y * cos_theta - z * sin_theta)
        node[2] = rotation_center[2] + (z * cos_theta + y * sin_theta)


def rotate_y_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        x, z = node[0] - rotation_center[0], node[2] - rotation_center[2]
        node[0] = rotation_center[0] + (x * cos_theta - z * sin_theta)
        node[2] = rotation_center[2] + (z * cos_theta + x * sin_theta)


cube = Cuboid((100, 100, 100), (200, 200, 200))
cone = Pyramid((100, 100, 100), (200, 200, 200))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[0]:
                pass
                rotate_y_shape(event.rel[0], cone.nodes, (200, 200, 200))
                rotate_x_shape(event.rel[1], cone.nodes, (200, 200, 200))
                rotate_y_shape(event.rel[0], cube.nodes, cube.center)
                rotate_x_shape(event.rel[1], cube.nodes, cube.center)

    screen.fill(pygame.Color('white'))
    cone.draw(screen)
    cube.draw(screen)
    pygame.display.flip()
pygame.quit()
