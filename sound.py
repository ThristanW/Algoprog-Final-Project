import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'Algoprog/Final Project/resources/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'PistolFire.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'enemy-pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'death-1.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'EnemySmgFire.wav')
