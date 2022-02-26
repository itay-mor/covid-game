import pygame.sprite
from pygame.sprite import Group

from player import Player
from settings import TILE_SIZE
from spritesheet import SpriteSheet
from tile import Tile


class Level:
    players: Group
    tiles: Group

    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.sprite_sheet = SpriteSheet(r'assets/Standard sprites upd.png')
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        enemy = self.sprite_sheet.image_at((16 * 7, 16, 16, 16))
        enemy_rect = enemy.get_rect(center=(150, 50))
        self.player1 = Player(self.sprite_sheet, self.players)
        self.player2 = Player(self.sprite_sheet, self.players)

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE

                    tile = Tile((x, y), TILE_SIZE, self.tiles)

    def horizontal_movement_collision(self):
        player = self.player1
        player.rect.x += player.direction.x

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left

    def vertical_movement_collision(self):
        player = self.player1
        player.apply_gravity()
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom

    def run(self):
        self.players.update()
        self.vertical_movement_collision()
        self.horizontal_movement_collision()
        self.tiles.draw(self.display_surface)
        self.players.draw(self.display_surface)
