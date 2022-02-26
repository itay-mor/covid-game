import random
from typing import Any

import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet, *groups):
        super().__init__(*groups)
        self.jump_speed = -6
        self.gravity = 0.8
        self.current_ground = HEIGHT
        self.image = sprite_sheet.image_at((16, 16, 16, 16))
        randint = random.randint(0, WIDTH)
        self.rect = self.image.get_rect(bottomleft=(randint, HEIGHT - 100))
        self.direction = pygame.math.Vector2(0, 0)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.get_input()
        #
        # if self.rect.bottom >= HEIGHT:
        #     self.rect.bottom = HEIGHT

    def get_input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        if keys[pygame.K_UP]:
            self.jump()

        if keys[pygame.K_RIGHT]:
            self.direction.x += 1

        if keys[pygame.K_LEFT]:
            self.direction.x -= 1

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
