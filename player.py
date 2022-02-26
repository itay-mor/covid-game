import random
from typing import Any

import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet, *groups):
        super().__init__(*groups)
        self.gravity = 0
        self.current_ground = HEIGHT
        self.image = sprite_sheet.image_at((16, 16, 16, 16))
        randint = random.randint(0, WIDTH)
        self.rect = self.image.get_rect(bottomleft=(randint, HEIGHT))
        # self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)

        self.gravity += 0.5
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.rect.bottom >= HEIGHT:
            self.gravity = -6

        if key[pygame.K_RIGHT]:
            self.rect.x += 1

        self.rect.y += self.gravity

        if key[pygame.K_LEFT]:
            self.rect.x -= 1
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT