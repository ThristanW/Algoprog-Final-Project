import random
import os
import pygame as pg
from sprite_object import *
from npc import *
from npc_2 import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'Algoprog/Final Project/resources/npc/'
        self.static_sprite_path = 'Algoprog/Final Project/resources/static_sprites'
        self.anim_sprite_path = 'Algoprog/Final Project/resources/animated_sprites'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
       
        #sprite map
        add_sprite(SpriteObject(game))
        add_sprite(AnimatedSprite(game))

        #npc map
        add_npc(NPC(game))
        add_npc(NPC(game))
        add_npc(NPC(game))
        add_npc(NPC(game))
        add_npc(NPC_2(game))
        add_npc(NPC_2(game))
        add_npc(NPC_2(game))
        add_npc(NPC_2(game))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        [npc_2.update() for npc_2 in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)