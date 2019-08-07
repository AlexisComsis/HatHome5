import pygame as pg
vec = pg.math.Vector2
from settings import *


class Gold45(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.weapons
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.gun_distance = GOLD45_DISTANCE

        self.image_bank_lvl1 = game.gold45_image_bank_lvl1
        self.image_bank_lvl2 = game.gold45_image_bank_lvl2
        self.image_bank_lvl3 = game.gold45_image_bank_lvl3
        self.image_bank_lvl4 = game.gold45_image_bank_lvl4

        self.image = self.image_bank_lvl1[0]
        self.image_old = self.image
        self.real_rect = self.image.get_rect()
        self.rect = self.real_rect
        self.real_rect.center = vec(0,0)
        self.pos = self.real_rect.center
        self.last_shot = 0
        self.lvl = 1
        self.cd = 0
        self.sharp_ready = True
        self.triangle = 1
        self.testweapons = 0
        self.fire = False


    def update(self):

        if self.cd > 0:
            self.cd -= 1

        if self.game.player.keys[pg.K_u] and self.cd == 0:
            self.lvl_up()

            self.cd = 20
        if self.game.player.keys[pg.K_p] and self.cd == 0:
            self.lvl_down()
            self.cd = 20


        if self.lvl == 1:
            self.move(self.image_bank_lvl1)
            self.fire_lvl1()
        if self.lvl == 2:
            self.move(self.image_bank_lvl2)
            self.fire_lvl2()
        if self.lvl == 3:
            self.move(self.image_bank_lvl3)
            self.fire_lvl2()
        if self.lvl == 4:
            self.move(self.image_bank_lvl4)
            self.fire_lvl2()

    def lvl_up(self):
        if self.lvl < 4:
            self.lvl += 1

    def lvl_down(self):
        if self.lvl > 1:
            self.lvl -= 1
    countime = 0
    def move(self, bank):
        if self.fire:
            pass
        else:
            self.translator = vec(self.game.camera.camera.x, self.game.camera.camera.y) # map --> screen
            self.mousepossc = self.game.mousepos - self.translator # map --> mouse
            self.vector = self.mousepossc - self.game.player.pos  # player(refer to map) --> mouse(refer to map)
            self.rot = self.vector.angle_to(vec(self.gun_distance, 0))
            if ((self.rot < -90) or (self.rot > 90)):
                self.image_old = bank[1]
            else:
                self.image_old = bank[0]
            self.vecvec = vec(self.gun_distance, 0).rotate(-(self.rot))
            self.image = pg.transform.rotate(self.image_old, self.rot)
            self.real_rect.center = self.game.player.real_rect.center + self.vecvec

    def fire_lvl1(self):
        if self.game.player.mouse[0]:
            now = pg.time.get_ticks()
            if now - self.last_shot > GOLD45_BULLET_FIRECOOLDOWN:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = (self.game.player.pos) + dir * 70
                Gold45_bullet(self.game, pos)

    def fire_lvl2(self):

        if self.game.player.mouse[2]:
            now = pg.time.get_ticks()

            if now - self.last_shot > GOLD45_BULLET_SHARP_FIRECOOLDOWN:
                self.last_shot = now
                dir = vec(1, 0).rotate(-self.rot)
                pos = (self.game.player.pos) + dir * 75
                Gold45_bullet_sharp(self.game, pos)

        self.fire_lvl1()

    def fire_lvl3(self):
        self.fire_lvl2()

    def fire_lvl4(self):
        self.fire_lvl2()



class Gold45_bullet(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.gold45_image_bank_lvl1[2]
        self.image_old = self.image

        self.rect = self.image.get_rect()
        self.real_rect = self.rect
        self.real_rect.center = (pos)
        self.pos = vec(self.real_rect.center)
        self.vector = self.game.player.gun.mousepossc - self.pos
        self.rot = self.vector.angle_to(vec(1, 0))

        self.image = pg.transform.rotate(self.image_old, self.rot)
        #self.real_rect.center = pos
        self.bulletlifetime = GOLD45_BULLET_LIFETIME
        self.vel = self.game.player.gun.vecvec * GOLD45_LVL1_BULLET_SPEED
        #spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        #self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()



    def update(self):
        if pg.sprite.spritecollideany(self, self.game.walls) or pg.sprite.spritecollideany(self, self.game.ships):
            self.kill()

        hits = pg.sprite.groupcollide(self.game.mobs, self.game.bullets, False, True)
        for hit in hits:
            hit.vel -= hit.vel/1.5
            hit.life -= GOLD45_DAMAGE
            hit.aware = 5000

        self.pos += self.vel * self.game.dt
        self.real_rect.center = self.pos



        if pg.time.get_ticks() - self.spawn_time > self.bulletlifetime:
            self.kill()


class Gold45_bullet_sharp(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.bulletssharp
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.gold45_image_bank_lvl4[2]
        self.image_old = self.image

        self.real_rect = self.image.get_rect()
        self.real_rect.center = (pos)
        self.pos = vec(self.real_rect.center)
        self.vector = self.game.player.gun.mousepossc - self.pos
        self.rot = self.vector.angle_to(vec(1, 0))

        self.image = pg.transform.rotate(self.image_old, self.rot)
        #self.real_rect.center = pos
        self.bulletlifetime = GOLD45_BULLET_LIFETIME
        self.vel = self.game.player.gun.vecvec * GOLD45_LVL2_BULLET_SPEED
        #spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        #self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def activate(self):

        self.kill()

    def update(self):

        hits2 = pg.sprite.groupcollide(self.game.bulletssharp, self.game.bullets, False, True)
        for hit in hits2:
            self.activate()

        if pg.sprite.spritecollideany(self, self.game.walls) or pg.sprite.spritecollideany(self, self.game.ships):
            self.kill()

        hits = pg.sprite.groupcollide(self.game.mobs, self.game.bulletssharp, False, True)
        for hit in hits:
            hit.vel -= hit.vel/1.5
            hit.life -= GOLD45_SHARP_DAMAGE
            hit.aware = 5000


        self.pos += self.vel * self.game.dt
        self.real_rect.center = self.pos

        if pg.time.get_ticks() - self.spawn_time > self.bulletlifetime:
            self.kill()
