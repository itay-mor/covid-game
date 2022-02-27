from typing import Any

import pygame

from player import Player
from spritesheet import SpriteSheet


class Enemy(Player):
    def __init__(self, sprite_sheet: SpriteSheet, *groups):
        super().__init__(sprite_sheet, 0, *groups)
        self.image = self.sprite_sheet.image_at((16*7, 16, 16, 16))
        self.used_keys['jump'] = 0
        self.used_keys['left'] = 0
        self.used_keys['right'] = 0
        self.joysticks = [pygame.joystick.Joystick(i) for i in  range(pygame.joystick.get_count())]

    def update(self, *args: Any, **kwargs: Any) -> None:
        super(Enemy, self).update()
        for joystick in self.joysticks:
            if joystick.get_button(0) or joystick.get_axis(1) < -0.1:
                self.direction.y = self.jump_speed
            axis0 = joystick.get_axis(0)
            # if axis0 < -0.1 or axis0 > 0.1:
            self.direction.x = axis0 + 0.1
            # print(f'axis: {axis0}')
            # print(f'direction: {self.direction.x}')
