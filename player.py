import random
from typing import Any

import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet, jump_key: int, *groups):
        super().__init__(*groups)
        self.jump_speed = -6
        self.gravity = 0.8
        self.sprite_sheet = sprite_sheet
        self.image = self.sprite_sheet.image_at((16, 16, 16, 16))
        randint = random.randint(0, WIDTH)
        self.rect = self.image.get_rect(bottomleft=(randint, HEIGHT - 100))
        self.direction = pygame.math.Vector2(0, 0)
        self.used_keys = {
            'jump': pygame.K_UP if jump_key == pygame.K_UP else pygame.K_w,
            'left': pygame.K_LEFT if jump_key == pygame.K_UP else pygame.K_a,
            'right': pygame.K_RIGHT if jump_key == pygame.K_UP else pygame.K_d,
        }

    # def import_character_assets(self):
    # self.animation = {
    #     'idle': self.sprite_sheet.image_at((16, 16, 16, 16))
    #     'run'
    # }

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.get_input()
        #
        # if self.rect.bottom >= HEIGHT:
        #     self.rect.bottom = HEIGHT

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        if keys[self.used_keys['jump']]:
            self.jump()

        if keys[self.used_keys['right']]:
            self.direction.x += 1

        if keys[self.used_keys['left']]:
            self.direction.x -= 1

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
