import pygame as pg
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS     #setting the initial position of player
        self.angle = PLAYER_ANGLE    
        self.shot = False   

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0                                   #starting position  
        speed = PLAYER_SPEED * self.game.delta_time     #the amount of time that has passed since the last frame
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed() #setting movement keys
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        #if keys[pg.K_LEFT]:                                         #setting camera rotation 
        #    self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        #if keys[pg.K_RIGHT]:
        #    self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau                                      #tau = 2*pi

    def check_wall(self, x, y):                         #checking for walls in the game at a given position (x, y)
        return (x, y) not in self.game.map.world_map    #if the position (x, y) is not found in the self.game.map.world_map definition located in the map module, no wall is considered, allowing the player to move, and vice versa.
    
    def check_wall_collision(self, dx, dy):                 #checks for the direction (dx, dy) the player is moving in and checks if a collision occurs
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx                                    #if there are no walls detected, self.x and self.y updates, indicating that the player has moved.    
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self): 
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),          #drawing a line to indicate where the player is facing
        #            (self.x * 100 + WIDTH * math.cos(self.angle),
        #             self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)     #drawing the player as a circle

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y
        
    @property
    def map_pos(self):
        return int(self.x), int(self.y)