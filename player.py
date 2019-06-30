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

def collide_with_collidem(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        for hit in hits:
            vec1 = (sprite.game.player.pos - sprite.pos).length()
            vec2 = (hit.game.player.pos - hit.pos).length()
            distance = abs((vec1 - vec2)/100)
            if distance < 0.01:
                distance = 0.01


            if sprite.vel.x > 0:
                if vec1 > vec2:
                    sprite.vel.x -= (5/distance) + sprite.vel.x/25
                    hit.vel.x += (5/distance) + sprite.vel.x/25
                #    if sprite.vel.x < 50:
                #        sprite.vel.x = 50
            if sprite.vel.x < 0:
                if vec1 > vec2:
                    sprite.vel.x += (5/distance) + sprite.vel.x/25
                    hit.vel.x -= (5/distance) + sprite.vel.x/25

                    #if sprite.vel.x > -50:
                        #sprite.vel.x = -50

            sprite.real_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        for hit in hits:
            vec1 = (sprite.game.player.pos - sprite.pos).length()
            vec2 = (hit.game.player.pos - hit.pos).length()
            distance = abs((vec1 - vec2)/100)
            if distance < 0.01:
                distance = 0.01

            if sprite.vel.y > 0:
                if vec1 > vec2:
                    sprite.vel.y -= (5/distance) + sprite.vel.y/25
                    hit.vel.y += (5/distance) + sprite.vel.y/25
            if sprite.vel.y < 0 :
                if vec1 > vec2:
                    sprite.vel.y += (5/distance) + sprite.vel.y/25
                    sprite.vel.y -= (5/distance) + sprite.vel.y/25
            sprite.hit_rect.centery = sprite.pos.y

def collide_with_collide(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        for hit in hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hit.real_rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hit.real_rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.real_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        for hit in hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hit.real_rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hit.real_rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


def mobs_attack(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.vel.x -= 100
            if sprite.vel.x < 0:
                sprite.vel.x += 100

            sprite.hit_rect.centerx = sprite.pos.x


            if hits[0].game.player.cooldown == 0:
                hits[0].game.player.cooldown += 35
                hits[0].game.player.life -= sprite.damage


    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.vel.y -= 10
            if sprite.vel.y < 0:
                sprite.vel.y += 10
            sprite.hit_rect.centery = sprite.pos.y

            if hits[0].game.player.cooldown == 0:
                hits[0].game.player.cooldown += 35
                hits[0].game.player.life -= sprite.damage



class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.playersprite
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.bank_image = game.player_image_bank
        self.image = game.player_image_bank[0]
        self.real_rect = self.image.get_rect()
        self.rect = self.real_rect
        self.hit_rect = self.real_rect
        self.hit_rect.center = self.real_rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.moovestat = 0
        self.timer = 0
        self.max_life = 200
        self.life = 200
        self.max_stamina = 100
        self.stamina = 100
        # Weapons
        self.gun = Gold45(self.game)
        self.selectgun = 0
        #self.sword = Sword()
        #self.magic = Magic()
        self.cd = 0
        self.invincibility = False


    def get_keys(self):
        self.vel = vec(0, 0)
        self.keys = pg.key.get_pressed()
        self.mouse = pg.mouse.get_pressed()
        if self.cd > 0:
            self.cd -= 1
        if self.keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if self.keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if self.keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if self.keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.keys[pg.K_LSHIFT] and (self.vel.y != 0 or self.vel.x != 0):
            if self.stamina > 0:
                self.vel.x = self.vel.x * 1.5
                self.vel.y= self.vel.y * 1.5
                self.stamina -= 0.65
                self.timer += 2

        elif self.stamina < 100:
            self.stamina += 0.50
        if self.stamina < 0:
            self.stamina = 0
        if self.stamina > 100:
            self.stamina = 100

        if self.keys[pg.K_f]:
            if self.selectgun == 0 and self.cd == 0 :
                self.gun.kill()
                self.gun = Wavax(self.game)
                self.gun.real_rect.center = (-10000,-10000)
                self.selectgun = 1
                self.cd = 50

            elif self.selectgun != 0 and self.cd == 0:
                self.gun.kill()
                self.gun = Gold45(self.game)
                self.gun.real_rect.center = (-10000,-10000)
                self.selectgun = 0
                self.cd = 50

        if self.vel.x != 0 or self.vel.y != 0:
            self.footupdate()
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071



    def get_mouse(self):


        mouse = pg.mouse.get_pos()

        x = mouse[0]
        y = mouse[1]

        if y >= HEIGHT/2: #BOTTOM
            if x >= WIDTH/2: #RIGHT BOTTOM
                if  DIAGONAL * x < y : #BOTTOM TRIANGLE
                    self.image = self.bank_image[0+self.moovestat]
                    self.gun.triangle = 7
                else:
                    self.image = self.bank_image[2+self.moovestat]
                    self.gun.triangle = 8
            else: #LEFT BOTTOM
                if DIAGONAL * (-x) + HEIGHT < y : #TOP TRIANGLE
                    self.image = self.bank_image[14+self.moovestat]
                    self.gun.triangle = 6
                else:
                    self.image = self.bank_image[12+self.moovestat]
                    self.gun.triangle = 5
        else: #TOP
            if x <= WIDTH/2: #LEFT TOP
                if DIAGONAL * x < y : #BOTTOM TRIANGLE
                    self.image = self.bank_image[10+self.moovestat]
                    self.gun.triangle = 4
                else:
                    self.image = self.bank_image[8+self.moovestat]
                    self.gun.triangle = 3
            else: #RIGHT TOP
                if DIAGONAL * (-x) + HEIGHT < y : #TOP TRIANGLE
                    self.image = self.bank_image[4+self.moovestat]
                    self.gun.triangle = 1
                else:
                    self.image = self.bank_image[6+self.moovestat]
                    self.gun.triangle = 2
        print(self.invincibility)
        if self.invincibility:
            self.image = pg.Surface((self.rect.width, self.rect.height))
            self.image.set_alpha(0)


    def footupdate(self):
        self.timer += 1

        if self.timer <=15:
            self.moovestat = 0
        elif self.timer <= 31:
            self.moovestat = 1
        else:
            self.timer = 0

    def update(self):
        Player.countime += 1
        print(Player.countime)
        #MOUVEMENT
        self.get_keys()
        self.pos += self.vel * self.game.dt

        self.hit_rect.centery = self.pos.y
        collide_with_collide(self, self.game.collidewithplayer, 'y')
        self.hit_rect.centerx = self.pos.x
        collide_with_collide(self, self.game.collidewithplayer, 'x')
        self.real_rect.center = self.hit_rect.center
        #MOUSE
        self.get_mouse()

        if Player.countime < INVINCIBILITY_TIME and Player.countime%10 < 5:
            self.invincibility = True
        else:
            self.invincibility = False

    def draw_player_health(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 260
        BAR_HEIGHT = 30
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_player_stamina(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 160
        BAR_HEIGHT = 30
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, PURPLE, outline_rect, 3)

    countime = INVINCIBILITY_TIME+1
    def beattack(self, mob):
        if Player.countime > INVINCIBILITY_TIME:
            self.life -= mob.damage
            Player.countime = 0
