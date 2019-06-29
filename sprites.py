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
        self.cooldown = 0
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


    def footupdate(self):
        self.timer += 1

        if self.timer <=15:
            self.moovestat = 0
        elif self.timer <= 31:
            self.moovestat = 1
        else:
            self.timer = 0

    def update(self):
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
        if self.cooldown > 0:
            self.cooldown -= 1

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
        self.distance = sqrt(self.distance[0]**2 + self.distance[1]**2)

        if self.life <= 0:
            randstat = int(random.random() * 100)
            if randstat <= self.dropchest:
                Chest(self.game, self.pos)
            self.state = False
            self.kill()


        if self.state:
            if self.distance < self.aware:
                self.bank_image = self.bank_angry_image

                self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
                self.footupdate()
                self.get_dir()
                #self.image = pg.transform.rotate(self.game.globu_img, self.rot)
                self.real_rect = self.image.get_rect()
                self.real_rect.center = self.pos
                self.acc = vec(GLOBU_SPEED, 0).rotate(-self.rot)
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                if hypot(vec(self.game.player.pos - self.pos).x, vec(self.game.player.pos - self.pos).y) <= 20:
                    pass
                else:
                    self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt **1.2 #manipuler

                self.game.collidewithmobs.remove(self)
                self.hit_rect.centerx = self.pos.x
                collide_with_collide(self, self.game.collidewithmobs2, 'x')
                collide_with_collidem(self, self.game.collidewithmobs, 'x')
                mobs_attack(self, self.game.playersprite, 'x')
                self.hit_rect.centery = self.pos.y
                collide_with_collide(self, self.game.collidewithmobs2, 'y')
                collide_with_collidem(self, self.game.collidewithmobs, 'y')
                mobs_attack(self, self.game.playersprite, 'y')
                self.real_rect.center = self.hit_rect.center
                self.game.collidewithmobs.add(self)

            else :
                self.rot = (self.game.ship.pos - self.pos).angle_to(vec(1, 0))
                self.footupdate()
                self.get_dir()
                self.real_rect = self.image.get_rect()
                self.real_rect.center = self.pos
                self.acc = vec(GLOBU_SPEED, 0).rotate(-self.rot)
                self.acc += self.vel * -1
                self.vel += self.acc * self.game.dt
                self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt **1.2 #manipuler
                self.game.collidewithmobs.remove(self)
                self.hit_rect.centerx = self.pos.x
                collide_with_collidem(self, self.game.collidewithmobs, 'x')
                collide_with_collide(self, self.game.collidewithmobs2, 'x')
                mobs_attack(self, self.game.playersprite, 'x')
                self.hit_rect.centery = self.pos.y
                collide_with_collidem(self, self.game.collidewithmobs, 'x')
                collide_with_collide(self, self.game.collidewithmobs2, 'y')
                mobs_attack(self, self.game.playersprite, 'y')
                self.real_rect.center = self.hit_rect.center
                self.game.collidewithmobs.add(self)



    class Bar(pg.sprite.Sprite):
        def __init__(self, MOB, game):
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.col = (0,0,255)
            self.mob = MOB
            self.image = pg.Surface(((self.mob.life / self.mob.max_life) * self.mob.real_rect.width, 10))
            self.image.fill(self.col)
            self.real_rect = self.image.get_rect()
            self.rect = self.real_rect

        def update(self):
            if self.mob.life > int((self.mob.max_life/3)*2):
                self.col = GREEN
            elif self.mob.life > int(self.mob.max_life/3):
                self.col = YELLOW
            else:
                self.col = RED
            if self.mob.life > 0:
                self.image = pg.Surface(((self.mob.life / self.mob.max_life) * self.mob.real_rect.width, 6))
                self.image.fill(self.col)
            else:
                self.kill()
            self.real_rect.x = self.mob.real_rect.x
            self.real_rect.y = self.mob.real_rect.y - 6



'''

  def draw_health(self):
        if self.health > 60:
            col = GREEN
        elif self.health > 30:
            col = YELLOW
        else:
            col = RED
        width = int(self.rect.width * self.health / MOB_HEALTH)
        self.health_bar = pg.Rect(0, 0, width, 7)
        if self.health < MOB_HEALTH:
            pg.draw.rect(self.image, col, self.health_bar)
'''


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, wall):
        self.groups = game.all_sprites, game.walls, game.collidewithplayer, game.collidewithmobs2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_bank = game.wall_image_bank
        self.image = self.image_bank[wall]
        self.real_rect = self.image.get_rect()
        self.rect = self.real_rect
        self.x = x
        self.y = y
        self.real_rect.x = x * TILESIZE
        self.real_rect.y = y * TILESIZE

class Ground(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grounds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_bank = game.ground_image_bank
        self.image = self.image_bank[0]
        self.rect = self.image.get_rect()
        self.real_rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.real_rect.x = x * TILESIZE
        self.real_rect.y = y * TILESIZE

class Ship(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.ships, game.collidewithplayer, game.collidewithmobs2
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_bank = game.ship_image_bank
        self.image = self.image_bank[0]
        self.rect = self.image.get_rect()
        self.real_rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.real_rect.x = x * TILESIZE
        self.real_rect.y = y * TILESIZE
        self.max_life = 1000
        self.life = 1000
        self.pos = vec(x, y) * TILESIZE
