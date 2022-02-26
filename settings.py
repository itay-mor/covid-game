from spritesheet import SpriteSheet

level_map = [
    '                            ',
    '                      XX    ',
    '                            ',
    '               XXXXXXXXXX   ',
    '                            ',
    '     XXXXXXXXXX             ',
    '                            ',
    '               XXXXXX       ',
    '                            ',
    '                            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

SCALE_FACTOR = 4
TILE_SIZE = 16
WIDTH, HEIGHT = (len(level_map[0]) * TILE_SIZE, len(level_map) * TILE_SIZE)

