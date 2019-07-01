import pygame as pg
from settings import *
from chest import *
vec = pg.math.Vector2
from math import hypot
from tilemap import collide_hit_rect
import random
from math import *
from gold45 import *
from wavax import *

class Ship(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.ships, game.collidewithplayer, game.collidewithmobs2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_bank = game.ship_image_bank
        self.image = self.image_bank[0].copy()
        self.rect = self.image.get_rect()
        self.real_rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.real_rect.x = x * TILESIZE
        self.real_rect.y = y * TILESIZE
        self.max_life = 1000
        self.life = 1000
        self.pos = vec(x, y) * TILESIZE

    def update(self):
        h = (self.life / self.max_life) * self.image_bank[1].get_height()
        if h<=0:
            h=0
        self.image = self.image_bank[0].copy()
        empty = (self.image_bank[1].copy()).subsurface((0,0, self.image_bank[1].get_width(), self.image_bank[1].get_height()-h))
        self.image.blit(empty, (75, 48))

    def beattack(self, mob):
        self.life -= 0.2
