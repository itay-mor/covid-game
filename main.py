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
level = Level(level_map, screen)

sprites = pygame.sprite.Group()
# player1 = Player(SPRITE_SHEET, sprites)
# player2 = Player(SPRITE_SHEET, sprites)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP and player1_rect.bottom >= HEIGHT:
        #         player1_gravity = -6
    # Player
    # player1_gravity += 0.5
    # player1_rect.y += player1_gravity
    # if player1_rect.bottom >= HEIGHT:
    #     player1_rect.bottom = HEIGHT

    screen.blit(background, (0, 0))
    level.run()
    sprites.draw(screen)

    scaled_screen = pygame.transform.scale(screen, display.get_size())
    display.blit(scaled_screen, (0, 0))
    pygame.display.update()
    clock.tick(60)
