import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface((size, 3))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft=pos)
