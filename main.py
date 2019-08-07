import pygame as pg
import sys
from os import path
from settings import *
#from player ship ground globuzar wall ground import *
from tilemap import *
from player import *
from ship import *
from ground import *
from globuzar import *
from wall import *
from ground import *
from constructor import *
from menu import *

#from gold45 import *
#from wavax import *


class Game:

    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(50, 100)
        self.constructor = Constructor(self)

    def new(self):
        #pg.mixer.music.play(-1)
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.hud = pg.sprite.Group()
        self.collidewithplayer = pg.sprite.Group()
        self.collidewithmobs = pg.sprite.Group()
        self.collidewithmobs2 = pg.sprite.Group()
        self.chests = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grounds = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.weapons = pg.sprite.Group()
        self.playersprite = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.bulletssharp = pg.sprite.Group()
        self.ships = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '.':#Ground
                    Ground(self, col, row)
                elif tile == 'G' or tile == 'P' or tile == 'S':
                    Ground(self, col, row)


        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row)
                    #self.weapon = Gold(self)
                elif tile == 'G':
                    Mob(self, col, row)
                elif tile == 'S':
                    self.ship = Ship(self, col, row)



        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.mousepos = pg.mouse.get_pos()
        self.mousepos = vec(self.mousepos)
        self.mousex = self.mousepos[0]
        self.mousey = self.mousepos[1]
        self.all_sprites.update()
        self.camera.update(self.player)



    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.window, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.window, BLACK, (0, y), (WIDTH, y))

    def draw(self):
        self.window.fill(BGCOLOR)

        for sprite in self.all_sprites:
            sprite.rect = self.camera.apply(sprite)
        self.list = []
        self.list.append(self.player)
        self.list.append(self.player.gun)
        for mob in self.mobs:
            self.list.append(mob)

        for item in self.list:
            if self.player.gun.lvl == 4 and isinstance(item, Wavax):
                item.rect.centery += 8
        self.list.sort( key=lambda item: item.rect.centery)
        for item in self.list:
            if self.player.gun.lvl == 4 and isinstance(item, Wavax):
                item.rect.centery -= 8
            self.all_sprites.change_layer(item, self.list.index(item))
            try:
                self.all_sprites.change_layer(item.bar, self.list.index(item))
            except:
                pass
        self.all_sprites.draw(self.window)



        self.player.draw_player_stamina()
        self.player.draw_player_health()

        pg.display.flip()




    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
M = Menu()
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
