import pygame as pg

_ = False       #making '_' false
mini_map = [
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, _, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, 1, ],
[2, _, _, _, _, _, _, _, _, _, _, _, _, 2, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[2, 2, 2, 2, 2, _, _, _, _, 2, 2, 2, 2, 2, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, _, 1, _, 1, _, 1, _, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
[1, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
[1, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, 1, _, _, _, _, 1, _, _, _, _, 1],
[1, 1, 1, 1, 1, _, _, _, _, 1, 1, 1, 1, 1, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:                           #ignores false values '_' so they are left as empty spaces, True values are added to world_map     
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)  #generates borders on the walls of the map
            for pos in self.world_map]