import random
from typing import Any

import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet, jump_key: int, *groups):
        super().__init__(*groups)

        # Set the appearance of the player.
        self.sprite_sheet = sprite_sheet
        self.image = self.sprite_sheet.image_at((16, 16, 16, 16))
        self.sick = False

        randint = random.randint(0, WIDTH)
        self.rect = self.image.get_rect(bottomleft=(randint, HEIGHT - 100))

        # Movement controls.
        self.jump_speed = -10
        self.gravity = 0.8
        self.direction = pygame.math.Vector2(0, 0)

        # Set the current used keys.
        self.used_keys = {
            'jump': pygame.K_UP if jump_key == pygame.K_UP else pygame.K_w,
            'left': pygame.K_LEFT if jump_key == pygame.K_UP else pygame.K_a,
            'right': pygame.K_RIGHT if jump_key == pygame.K_UP else pygame.K_d,
        }

        # Player status
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.pacing_right = True

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.get_input()
        #
        # if self.rect.bottom >= HEIGHT:
        #     self.rect.bottom = HEIGHT

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        if keys[self.used_keys['jump']] and self.on_ground:
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
