import pygame
import math


pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True

cube_center = (200, 200, 200)
cube_nodes = [
    [100, 100, 100],
    [100, 100, 300],
    [100, 300, 100],
    [100, 300, 300],
    [300, 100, 100],
    [300, 100, 300],
    [300, 300, 100],
    [300, 300, 300]
]
cube_edges = [
    [0, 1],
    [1, 3],
    [3, 2],
    [2, 0],
    [4, 5],
    [5, 7],
    [7, 6],
    [6, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
]


def make_3d_shape():
    pass


def draw_shape(surface, nodes, edges, node_color=(34, 68, 204), edge_color=(40, 168, 107), node_size=10):
    for edge in edges:
        start_node, end_node = nodes[edge[0]], nodes[edge[1]]
        pygame.draw.line(surface, node_color, (start_node[0] + node_size // 2, start_node[1] + node_size // 2),
                         (end_node[0] + node_size // 2, end_node[1] + node_size // 2))
    for node in nodes:
        pygame.draw.ellipse(surface, edge_color, (node[0], node[1], node_size, node_size))


def rotateZ_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        x, y = node[0] - rotation_center[0], node[1] - rotation_center[1]
        node[0] = rotation_center[0] + (x * cos_theta - y * sin_theta)
        node[1] = rotation_center[1] + (y * cos_theta + x * sin_theta)


def rotateX_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        y, z = node[1] - rotation_center[1], node[2] - rotation_center[2]
        node[1] = rotation_center[1] + (y * cos_theta - z * sin_theta)
        node[2] = rotation_center[2] + (z * cos_theta + y * sin_theta)


def rotateY_shape(degrees, nodes, rotation_center):
    sin_theta = math.sin(math.radians(degrees))
    cos_theta = math.cos(math.radians(degrees))
    for node in nodes:
        x, z = node[0] - rotation_center[0], node[2] - rotation_center[2]
        node[0] = rotation_center[0] + (x * cos_theta - z * sin_theta)
        node[2] = rotation_center[2] + (z * cos_theta + x * sin_theta)


rotateY_shape(50, cube_nodes, cube_center)
rotateX_shape(15, cube_nodes, cube_center)
# rotateZ_shape(60, cube_nodes, cube_center)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[0]:
                rotateY_shape(event.rel[0], cube_nodes, cube_center)
                rotateX_shape(event.rel[1], cube_nodes, cube_center)

    screen.fill(pygame.Color('white'))
    draw_shape(screen, cube_nodes, cube_edges)
    pygame.display.flip()
pygame.quit()
