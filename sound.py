import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.pistol = pg.mixer.Sound(self.path + 'PistolFire.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'enemy-pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'death-1.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'EnemyPistolFire.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player-pain-2.wav')