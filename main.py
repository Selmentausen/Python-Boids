import pygame
from shapes_3d import Cuboid, Pyramid
from shapes_2d import Boid2D


pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((400, 400))
running = True
boid = Boid2D((100, 100), 50, 50)
# cube = Cuboid((100, 100, 100), (200, 200, 200))
# cone = Pyramid((100, 100, 100), (200, 200, 200), edge_color=(255, 0, 0), node_color=(0, 0, 0))
move = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                boid.set_rotation(0)
            if event.key == pygame.K_w:
                move = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move = False
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[0]:
                boid.rotate(-event.rel[0])
    screen.fill(pygame.Color('white'))
    if move:
        boid.move_forward(clock.get_time() / 1000)
    boid.draw(screen)
#     cube.draw(screen)
#     cone.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
