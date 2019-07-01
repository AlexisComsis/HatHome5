import pygame as pg
from settings import *
import random
from math import *
vec = pg.math.Vector2

class Wavax(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.weapons
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.gun_distance = WAVAX_DISTANCE
        self.bank_of_bank = tuple()
        self.image_bank_lvl1 = game.wavax_image_bank_lvl1
        self.image_bank_lvl2 = game.wavax_image_bank_lvl2
        self.image_bank_lvl3 = game.wavax_image_bank_lvl3
        self.image_bank_lvl4 = game.wavax_image_bank_lvl4
        self.image = self.image_bank_lvl1[0]
        self.image_old = self.image
        self.real_rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.real_rect.center = vec(0,0)
        self.pos = self.real_rect.center
        self.last_shot = 0
        self.energymax = 75
        self.energy = 75
        self.consum = 1.5
        #self.bar = Wavax.Bar(self, self.game)
        self.cd = 0
        self.lvl = 1
        self.triangle = 1
        self.additionalx = 0
        self.additionaly = 0
        self.testweapons = 0
        self.shoot = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
            self.move_lvl1()
            self.fire_lvl1()
        if self.lvl == 2:
            self.move_lvl2()
            self.fire_lvl2()
        if self.lvl == 3:
            self.move_lvl3()
            self.fire_lvl3()
        if self.lvl == 4:
            self.move_lvl4()
            self.fire_lvl4()
        self.vrombissement()

    def lvl_up(self):
        if self.lvl < 4:
            self.lvl += 1

    def lvl_down(self):
        if self.lvl > 1:
            self.lvl -= 1
        #self.displayenergy()

    def vrombissement(self):
        if self.shoot:
            self.real_rect.centerx += int(random.randrange(0, 5, 1))
            self.real_rect.centery += int(random.randrange(0, 5, 1))




    def move_lvl1(self):
        #self.rect.center = self.game.player.rect.center
        #self.game.player.pos # map --> player
        #self.game.mousepos # screen --> mouse

        self.translator = vec(self.game.camera.camera.x, self.game.camera.camera.y) # map --> screen
        self.mousepossc = self.game.mousepos - self.translator # map --> mouse
        self.vector = self.mousepossc - self.game.player.pos  # player(refer to map) --> mouse(refer to map)
        self.rot = self.vector.angle_to(vec(self.gun_distance, 0))
        #self.image_bank_lvl1[0] = pg.image.load(self.game.wavax_folder + WAVAX_LVL1_IMAGE).convert_alpha()
        if ((self.rot < -90) or (self.rot > 90)):
            self.image_old = self.image_bank_lvl1[1].copy()
            self.image_old.blit(self.battery( 3, 40, self.image_bank_lvl1[3].copy()), (3 , 0))

        else:
            self.image_old = self.image_bank_lvl1[0].copy()
            self.image_old.blit(self.battery( 3, 40, self.image_bank_lvl1[2].copy()), (3 , 0))

        self.vecvec = vec(self.gun_distance, 0).rotate(-(self.rot))
        self.image = self.image_old
        self.image = pg.transform.rotate(self.image_old, self.rot)
        self.levecteur = vec(-(self.image.get_width()/2),-(self.image.get_height()/2))
        self.real_rect.center = (self.game.player.real_rect.center )  + self.levecteur + vec(self.width/2, self.height/2) + self.vecvec
        self.shoot = False

    def battery(self, start_x, end_x, image_empty):
            length = end_x-start_x
            self.image_child = image_empty.subsurface(start_x, 0, length, self.image_old.get_height())
            self.widthempty = int((self.energy / self.energymax) * length)
            self.newwidthempty = length/2 - (self.widthempty - length/2)
            self.image_understand = self.image_child.subsurface(0, 0, self.newwidthempty , self.image_old.get_height())
            return self.image_understand


            '''
    def cut(self):
        if self.variable == 0 : #right
            self.image_child = self.image_bank_lvl1[2].subsurface(3, 0, 40-3, self.image_old.get_height())
            self.widthempty = int((self.energy / self.energymax) * 37)

            self.newwidthempty = 37/2 - (self.widthempty - 37/2)

            self.image_understand = self.image_child.subsurface(0, 0, self.newwidthempty , self.image_old.get_height())


            self.image_old.blit(self.image_understand, (3 , 0))

        else:

            pass

            '''

    def move_lvl2(self):

        #self.real_rect.center = self.game.player.real_rect.center
        #self.game.player.pos # map --> player
        #self.game.mousepos # screen --> mouse
        self.translator = vec(self.game.camera.camera.x, self.game.camera.camera.y) # map --> screen
        self.mousepossc = self.game.mousepos - self.translator # map --> mouse
        self.vector = self.mousepossc - self.game.player.pos  # player(refer to map) --> mouse(refer to map)
        self.rot = self.vector.angle_to(vec(self.gun_distance, 0))

        self.vecvec = vec(self.gun_distance, 0).rotate(-(self.rot))
        self.image = pg.transform.rotate(self.image_old, self.rot)
        if ((self.rot < -90) or (self.rot > 90)):
            self.image_old = self.image_bank_lvl2[1]
        else:
            self.image_old = self.image_bank_lvl2[0]
        self.levecteur = vec(-(self.image.get_width()/2),-(self.image.get_height()/2))
        self.real_rect.center = (self.game.player.real_rect.center )  + self.levecteur + vec(self.width/2, self.height/2) + self.vecvec
        self.shoot = False

    def move_lvl3(self):

        #self.real_rect.center = self.game.player.real_rect.center
        #self.game.player.pos # map --> player
        #self.game.mousepos # screen --> mouse
        self.translator = vec(self.game.camera.camera.x, self.game.camera.camera.y) # map --> screen
        self.mousepossc = self.game.mousepos - self.translator # map --> mouse
        self.vector = self.mousepossc - self.game.player.pos  # player(refer to map) --> mouse(refer to map)
        self.rot = self.vector.angle_to(vec(self.gun_distance, 0))

        self.vecvec = vec(self.gun_distance, 0).rotate(-(self.rot))
        self.image = pg.transform.rotate(self.image_old, self.rot)


        if ((self.rot < -90) or (self.rot > 90)):
            self.image_old = self.image_bank_lvl3[1]
        else:
            self.image_old = self.image_bank_lvl3[0]

        self.levecteur = vec(-(self.image.get_width()/2),-(self.image.get_height()/2))
        self.real_rect.center = (self.game.player.real_rect.center )  + self.levecteur + vec(self.width/2, self.height/2) + self.vecvec *1.2
        self.shoot = False


        #self.image.fill((255,255,255))

    def move_lvl4(self):

        #self.real_rect.center = self.game.player.real_rect.center
        #self.game.player.pos # map --> player
        #self.game.mousepos # screen --> mouse
        self.translator = vec(self.game.camera.camera.x, self.game.camera.camera.y) # map --> screen
        self.mousepossc = self.game.mousepos - self.translator # map --> mouse
        self.vector = self.mousepossc - self.game.player.pos  # player(refer to map) --> mouse(refer to map)
        self.rot = self.vector.angle_to(vec(self.gun_distance, 0))

        self.vecvec = vec(self.gun_distance, 0).rotate(-(self.rot))
        if ((self.rot < -90) or (self.rot > 90)):
            self.image_old = self.image_bank_lvl4[1]
        else:
            self.image_old = self.image_bank_lvl4[0]
        self.image = pg.transform.rotate(self.image_old, self.rot)




        self.levecteur = vec(-(self.image.get_width()/2),-(self.image.get_height()/2))
        self.real_rect.center = (self.game.player.real_rect.center )  + self.levecteur + vec(self.width/2, self.height/2) + self.vecvec *1.2
        self.shoot = False


        #self.image.fill((255,255,255))

    def fire_lvl1(self):
        if not self.energy < 0:
            if self.game.player.mouse[0]:
                self.shoot = True
                self.energy -= self.consum
                now = pg.time.get_ticks()
                if now - self.last_shot > WAVAX_BULLET_FIRECOOLDOWN:
                    self.last_shot = now

                    dir = vec(1, 0).rotate(-self.rot)
                    #dir = vec(1, 0).rotate(-self.rot)
                    #self.pos = self.real_rect.center

                    pos = (self.game.player.pos) + dir * 75 #+ BARREL_OFFSET.rotate(-self.rot)
                    #self.game.wavax_shot.stop()
                    #self.game.wavax_shot.play()

                    Wavax_bullet(self.game, pos)
                    #self.vel = vec(-KICKBACK, 0).rotate(-self.rot)
        if self.energy <= self.energymax and not self.game.player.mouse[0]:
            self.energy += self.consum*0.8

    def fire_lvl2(self):
        if not self.energy < 0:
            if self.game.player.mouse[0]:
                self.shoot = True
                self.energy -= self.consum
                now = pg.time.get_ticks()
                if now - self.last_shot > WAVAX_BULLET_FIRECOOLDOWN:
                    self.last_shot = now

                    dir = vec(1, 0).rotate(-self.rot)
                    #dir = vec(1, 0).rotate(-self.rot)
                    #self.pos = self.real_rect.center

                    pos = (self.game.player.pos) + dir * 100 #+ BARREL_OFFSET.rotate(-self.rot)
                    #self.game.wavax_shot.stop()
                    #self.game.wavax_shot.play()

                    Wavax_bullet(self.game, pos)
                    #self.vel = vec(-KICKBACK, 0).rotate(-self.rot)
        if self.energy <= self.energymax and not self.game.player.mouse[0]:
            self.energy += self.consum*2

    def fire_lvl3(self):
        if not self.energy < 0:
            if self.game.player.mouse[0]:
                self.shoot = True
                self.energy -= self.consum
                now = pg.time.get_ticks()
                if now - self.last_shot > WAVAX_BULLET_FIRECOOLDOWN:
                    self.last_shot = now

                    dir = vec(1, 0).rotate(-self.rot)
                    #dir = vec(1, 0).rotate(-self.rot)
                    #self.pos = self.real_rect.center

                    pos = (self.game.player.pos) + dir * 125 #+ BARREL_OFFSET.rotate(-self.rot)
                    #self.game.wavax_shot.stop()
                    #self.game.wavax_shot.play()

                    Wavax_bullet(self.game, pos)
                    #self.vel = vec(-KICKBACK, 0).rotate(-self.rot)
        if self.energy <= self.energymax and not self.game.player.mouse[0]:
            self.energy += self.consum*0.8

    def fire_lvl4(self):
        if not self.energy < 0:
            if self.game.player.mouse[0]:
                self.shoot = True
                self.energy -= self.consum
                now = pg.time.get_ticks()
                if now - self.last_shot > WAVAX_BULLET_FIRECOOLDOWN:
                    self.last_shot = now


                    dir = vec(1, 0).rotate(-self.rot)
                    #dir = vec(1, 0).rotate(-self.rot)
                    #self.pos = self.real_rect.center

                    pos = (self.game.player.pos) + dir * 150 #+ BARREL_OFFSET.rotate(-self.rot)
                    #self.game.wavax_shot.stop()
                    #self.game.wavax_shot.play()

                    Wavax_bullet(self.game, pos)
                    #self.vel = vec(-KICKBACK, 0).rotate(-self.rot)
        if self.energy <= self.energymax and not self.game.player.mouse[0]:
            self.energy += self.consum*0.8

class Wavax_bullet(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.game.wavax_image_bank_lvl1[4]
        self.image_old = self.image
        self.rect = self.image.get_rect()
        self.real_rect = self.image.get_rect()
        self.real_rect.center = (pos)
        self.pos = vec(self.real_rect.center)
        self.vector = self.game.player.gun.mousepossc - self.pos
        self.rot = self.vector.angle_to(vec(1, 0))

        self.image = pg.transform.rotate(self.image_old, self.rot)
        #self.real_rect.center = pos
        self.bulletlifetime = WAVAX_BULLET_LIFETIME
        self.vel = self.game.player.gun.vecvec * WAVAX_BULLET_SPEED
        #spread = uniform(-GUN_SPREAD, GUN_SPREAD)
        #self.vel = dir.rotate(spread) * BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * self.game.dt
        self.real_rect.center = self.pos
        if pg.sprite.spritecollideany(self, self.game.walls) or pg.sprite.spritecollideany(self, self.game.ships):
            self.kill()

        hits = pg.sprite.groupcollide(self.game.mobs, self.game.bullets, False, True)
        for hit in hits:
            hit.vel -= hit.vel/35
            hit.life -= WAVAX_DAMAGE
            hit.aware = 5000


        if pg.time.get_ticks() - self.spawn_time > self.bulletlifetime:
            self.kill()
