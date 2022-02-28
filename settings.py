from spritesheet import SpriteSheet

level_map = [
    '                           ',
    '                       X X  ',
    '  X                         ',
    '  XX       XXXXX XXXXX      ',
    '          XX                ',
    '      X                XX    ',
    '                            ',
    '           XXXXX     XX     ',
    '        X         X         ',
    '       X      XXX     XXXX  ',
    ' XXXXX       X               ',
    '          XXX     X         ',
    '                            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

SCALE_FACTOR = 4
TILE_SIZE = 16
WIDTH, HEIGHT = (len(level_map[0]) * TILE_SIZE, len(level_map) * TILE_SIZE)

