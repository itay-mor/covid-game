import pygame

from level import Level
from player import Player
from settings import *
from tile import Tile

pygame.init()


enemy_gravity = 0

display = pygame.display.set_mode((WIDTH * SCALE_FACTOR, HEIGHT * SCALE_FACTOR))
screen = pygame.Surface((WIDTH, HEIGHT))

screen.fill((255, 123, 67))
background = screen.copy()
clock = pygame.time.Clock()

pygame.joystick.init()

l = Level(level_map, screen)

sprites = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.JOYBUTTONDOWN:
        #     if event.button == 0:
        #         # Enemy jump
        #         l.enemy.direction.y = l.enemy.jump_speed
        #         pass
        #
        # if event.type == pygame.JOYAXISMOTION:
        #     if event.axis in [0, 2]:
        #         l.enemy.direction.x += event.value


    screen.blit(background, (0, 0))
    l.run()
    sprites.draw(screen)

    scaled_screen = pygame.transform.scale(screen, display.get_size())
    display.blit(scaled_screen, (0, 0))
    pygame.display.update()
    clock.tick(60)
