import pygame
import math
from shapes import Cuboid, Pyramid

pygame.init()
screen = pygame.display.set_mode((400, 400))
running = True
cube = Cuboid((100, 100, 100), (200, 200, 200))
cone = Pyramid((100, 100, 100), (200, 200, 200), edge_color=(255, 0, 0), node_color=(0, 0, 0))

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
                cube.rotate_x(event.rel[1])
                cube.rotate_y(event.rel[0])
                cone.rotate_x(event.rel[1])
                cone.rotate_y(event.rel[0])
    screen.fill(pygame.Color('white'))
    cube.draw(screen)
    cone.draw(screen)
    pygame.display.flip()
pygame.quit()
