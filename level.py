import pygame.sprite
from pygame.sprite import Group

from enemy import Enemy
from player import Player
from settings import TILE_SIZE
from spritesheet import SpriteSheet
from tile import Tile


class Level:
    players: Group
    tiles: Group

    def __init__(self, level_data, surface):
        self.speed = 2
        self.display_surface = surface
        self.sprite_sheet = SpriteSheet(r'assets/Standard sprites upd.png')
        self.setup_level(level_data)
        pygame.joystick.init()
        self.enemy_x_motion = False

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.GroupSingle()
        self.enemy = Enemy(self.sprite_sheet, self.enemies)
        self.player1 = Player(self.sprite_sheet, pygame.K_UP, self.players)
        self.player2 = Player(self.sprite_sheet, pygame.K_w, self.players)
        self.player_list = [self.player1, self.player2, self.enemy]

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE

                    Tile((x, y), TILE_SIZE, self.tiles)

    def horizontal_movement_collision(self, player: Player):
        # player = self.player1
        player.rect.x += player.direction.x * self.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left

    def vertical_movement_collision(self, player):
        # player = self.player1
        player.apply_gravity()
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top

                    # Change the state of the player
                    player.on_ground = True

                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom

                    # Change the state of the player
                    player.on_ceiling = True

                player.direction.y = 0


            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False

            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False


    def move_players(self):
        for player in self.player_list:
            self.horizontal_movement_collision(player)
            self.vertical_movement_collision(player)

    def run(self):
            self.players.update()
            self.enemies.update()
            joysticks = [pygame.joystick.Joystick(i) for i in  range(pygame.joystick.get_count())]

            # self.vertical_movement_collision()
            # self.horizontal_movement_collision()
            self.move_players()
            for player in self.player_list[0:1]:
                if self.enemy.rect.colliderect(player.rect):
                    player.sick = True
                    # player.speed = 0
                    # player.jump_speed = 0


            self.tiles.draw(self.display_surface)
            self.players.draw(self.display_surface)
            self.enemies.draw(self.display_surface)
