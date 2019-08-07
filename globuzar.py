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

class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.timer = 0
        self.groups = game.all_sprites, game.mobs,  game.collidewithmobs #game.collidewithplayer,
        self.game = game
        pg.sprite.Sprite.__init__(self, self.groups)
        self.bank_image = game.globu_img_bank
        self.bank_angry_image = game.globu_angry_img_bank
        self.image = self.bank_image[0]
        self.real_rect = self.image.get_rect()
        self.rect = self.real_rect
        self.hit_rect = self.real_rect
        self.hit_rect.center = self.real_rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.real_rect.center = self.pos
        self.rot = 0
        self.col = (0,0,0)
        self.damage = 20
        self.life = 100
        self.max_life = 100
        self.state = True
        self.bar = Mob.Bar(self, self.game)
        self.aware = 600
        self.dropchest = GLOBU_DROPCHEST

    def footupdate(self):
        self.timer += 1

        if self.timer <=5:
            self.moovestat = 0
        elif self.timer <= 11 :
            self.moovestat = 1
        else:
            self.timer = 0

    def get_dir(self): #equivalent --> get_mouse() de plpayer
        if self.rot <= -135: #left down
            self.image = self.bank_image[12+self.moovestat]
        elif self.rot <= -90: #Down
            self.image = self.bank_image[14+self.moovestat]
        elif self.rot <= -45: #right down
            self.image = self.bank_image[0+self.moovestat]
        elif self.rot <= 0: #Right
            self.image = self.bank_image[2+self.moovestat]
        elif self.rot <= 45: #Top right
            self.image = self.bank_image[4+self.moovestat]
        elif self.rot <= 90:#Top
            self.image = self.bank_image[6+self.moovestat]
        elif self.rot <= 135:#Top left
            self.image = self.bank_image[8+self.moovestat]
        else: #left
            self.image = self.bank_image[10+self.moovestat]



    def update(self):
        self.distance = self.game.player.pos - self.pos
        self.distance = hypot(self.distance[0], self.distance[1])

        if self.life <= 0:
            self.state = False
            self.kill()
            self.bar.kill()
        else:
            if self.distance < self.aware:
                self.bank_image = self.bank_angry_image
                self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
            else :
                self.rot = (self.game.ship.pos - self.pos).angle_to(vec(1, 0))
            self.footupdate()
            self.get_dir()
            self.real_rect = self.image.get_rect()
            self.real_rect.center = self.pos
            self.acc = vec(GLOBU_SPEED, 0).rotate(-self.rot)
            self.acc += self.vel * -1
            self.vel += self.acc * self.game.dt
            self.move_collide()

    def move_collide(self):
        if self.rect.colliderect(self.game.player.rect):
            self.game.player.beattack(self)
        if self.rect.colliderect(self.game.ship.rect):
            self.game.ship.beattack(self)
        if hypot(vec(self.game.player.pos - self.pos).x, vec(self.game.player.pos - self.pos).y) <= GLOBU_RANGE_B_PLAYER:
            pass
        else:
            self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt **1.2 #manipuler


    class Bar(pg.sprite.Sprite):
        def __init__(self, MOB, game):
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.mob = MOB
            self.image_bank = self.game.globu_bar
            self.real_rect = self.image_bank[0].get_rect()
            self.rect = self.real_rect
            self.image = pg.Surface((self.image_bank[0].get_width(), self.image_bank[0].get_height()))

        def update(self):
            h = (self.mob.life / self.mob.max_life) * self.image_bank[0].get_width()
            if h<0:
                h = 0
            start = (self.image_bank[0].copy()).subsurface((0,0, h, self.image_bank[0].get_height()))
            self.image.blit(start, (0, 0))
            end = (self.image_bank[1].copy()).subsurface((h, 0, self.image_bank[0].get_width()-h, self.image_bank[0].get_height()))
            self.image.blit(end, (h, 0))
            self.real_rect.x = self.mob.real_rect.x
            self.real_rect.y = self.mob.real_rect.y - 12
