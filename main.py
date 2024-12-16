import pygame as pg         #pygame library import
import sys                  #system module import
from settings import *      #import settings
from map import *           #map import
from player import *        #player control import
from raycasting import *    #raycasting import
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__ (self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)  #setting up the window
        self.clock = pg.time.Clock()            #clock class (manages time based elements like FPS)
        self.delta_time = 1 
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 100)
        self.new_game()

    def new_game(self):                         
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        self.player.update()
        self.player.check_game_over()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()                                       #double buffering for smoothness
        self.delta_time = self.clock.tick(FPS)                  #limiting the FPS and obtaining delta time value
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')  #FPS counter

    def draw(self):   
        #self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        #self.map.draw()
        #self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):   
                pg.quit()                                                                           #if esc key is pressed, it quits pygame and exits the system
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):              #making the game loop
        while True:
            self.check_events() #checks to see if the escape key is pressed
            self.update()       
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()