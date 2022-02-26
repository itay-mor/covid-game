import pygame

from player import Player
from settings import *
from tile import Tile

pygame.init()


test_tile = pygame.sprite.Group(Tile((100, 100), 200))
player1_gravity = 0
player2_gravity = 0
enemy_gravity = 0

display = pygame.display.set_mode((WIDTH * SCALE_FACTOR, HEIGHT * SCALE_FACTOR))
screen = pygame.Surface((WIDTH, HEIGHT))
SPRITE_SHEET = SpriteSheet(r'assets/Standard sprites upd.png')
screen.fill((255, 123, 67))
background = screen.copy()
clock = pygame.time.Clock()

sprites = pygame.sprite.Group()
player1 = Player(SPRITE_SHEET, sprites)
player2 = SPRITE_SHEET.image_at((16, 16, 16, 16))
player2_rect = player2.get_rect(center=(250, 50))
enemy = SPRITE_SHEET.image_at((16 * 7, 16, 16, 16))
enemy_rect = enemy.get_rect(center=(150, 50))

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
    player1.update()
    sprites.draw(screen)
    test_tile.draw(screen)
    screen.blit(player2, player2_rect)
    screen.blit(enemy, enemy_rect)

    scaled_screen = pygame.transform.scale(screen, display.get_size())
    display.blit(scaled_screen, (0, 0))
    pygame.display.update()
    clock.tick(60)
