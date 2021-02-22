from settings import Settings
from shapes_2d import Boid2D
import pygame
import sys

pygame.init()
settings = Settings()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(settings.screen_size)
boid = Boid2D((100, 100), (30, 20))


def on_exit():
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on_exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                on_exit()
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[0]:
                boid.rotate(-event.rel[0])
    screen.fill(pygame.Color('black'))
    boid.update(screen, clock.get_time(), settings=settings)
    pygame.display.flip()
    clock.tick(settings.FPS)
