import random
from enum import Enum
from typing import Any

import pygame

from settings import *

class ControlDevice(Enum):
    KEYBOARD = 0
    JOYSTICK = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet, jump_key: int, control_device: ControlDevice, *groups):
        super().__init__(*groups)

        self.jump_music = pygame.mixer.Sound(r'assets/jump.mp3')
        self.jump_music.set_volume(0.35)

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

        self.control_device = control_device
        self.joysticks = [pygame.joystick.Joystick(i) for i in  range(pygame.joystick.get_count())]

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
        if self.control_device == ControlDevice.KEYBOARD:
            keys = pygame.key.get_pressed()
            self.direction.x = 0
            if keys[self.used_keys['jump']] and self.on_ground:
                self.jump()

            if keys[self.used_keys['right']]:
                self.direction.x += 1

            if keys[self.used_keys['left']]:
                self.direction.x -= 1
        else:
            for joystick in self.joysticks:
                if joystick.get_button(0) and self.on_ground:
                    self.jump()

                axis0 = joystick.get_axis(0) + 0.1
                self.direction.x = axis0 * 1.3

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
        self.jump_music.play()
