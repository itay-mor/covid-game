from spritesheet import SpriteSheet

level_map = [
    '                           ',
    '                       X X  ',
    '  X                         ',
    '  XX   X   XXXXX XXXXX      ',
    '                            ',
    '                      XX    ',
    '                            ',
    '           XXXXX     XX     ',
    '       XX                   ',
    '                      XXXX  ',
    ' XXXX                       ',
    '                            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

SCALE_FACTOR = 4
TILE_SIZE = 16
WIDTH, HEIGHT = (len(level_map[0]) * TILE_SIZE, len(level_map) * TILE_SIZE)

