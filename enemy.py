from typing import Any

import pygame

from player import Player, ControlDevice
from spritesheet import SpriteSheet


class Enemy(Player):
    def __init__(self, sprite_sheet: SpriteSheet, jump_key, control_device, *groups):
        super().__init__(sprite_sheet, jump_key, control_device, *groups)
        self.image = self.sprite_sheet.image_at((16*7, 16, 16, 16))
        self.jump_speed = -1
        self.speed = 1

    def update(self, *args: Any, **kwargs: Any) -> None:
        super(Enemy, self).update()
        self.get_input()

    def get_input(self):
        if self.control_device == ControlDevice.KEYBOARD:
            keys = pygame.key.get_pressed()
            self.direction.x = 0
            if keys[self.used_keys['jump']]:
                self.direction.y = self.jump_speed

            if keys[self.used_keys['right']]:
                self.direction.x += 1

            if keys[self.used_keys['left']]:
                self.direction.x -= 1

        else:
            for joystick in self.joysticks:
                if joystick.get_button(0):
                    self.direction.y = self.jump_speed

                axis0 = joystick.get_axis(0) + 0.1
                self.direction.x = axis0 * 0.5
