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

#from gold45 import *
#from wavax import *


class Constructor:

    def __init__(self, game):
        self.game = game
        self.load_data()

    def load_data(self):

        #folder
        self.game_folder = path.dirname(__file__)

        self.img_folder = path.join(self.game_folder, "Image")
        self.gold45_folder = path.join(self.img_folder, "Gold45")
        self.wavax_folder = path.join(self.img_folder, "Wavax")

        self.sound_folder = path.join(self.game_folder, "Sound")
        self.fire_sound_folder = path.join(self.sound_folder, 'FireSound')
        self.ship_folder = path.join(self.img_folder, 'Ship')

        #map music
        self.game.map = Map(path.join(self.game_folder, MAP))
        #self.music = pg.mixer.music.load(self.sound_folder + MUSIC)
        #pg.mixer.music.set_volume(1)
        #pg.mixer.music.play(-1)

        #player
        self.game.player_image_bank = self.separate(pg.image.load(self.img_folder + PLAYER_BANK_IMG).convert_alpha(), 78)
        self.game.player_life_image_bank = []
        self.game.player_life_image_bank.append(pg.image.load(self.img_folder + PLAYER_LIFE))
        self.game.player_life_image_bank.append(pg.image.load(self.img_folder + PLAYER_LIFE_EMPTY))
        self.game.player_stamina_image_bank = []
        self.game.player_stamina_image_bank.append(pg.image.load(self.img_folder + PLAYER_STAMINA))
        self.game.player_stamina_image_bank.append(pg.image.load(self.img_folder + PLAYER_STAMINA_EMPTY))

        #wall
        self.game.wall_image_bank = self.separate(pg.image.load(self.img_folder + WALL_IMG).convert_alpha(), 50) # LIST 4 ELEMENT
        self.game.wall_image_bank = self.wall_construct(self.game.wall_image_bank) #LIST 13 ELEMENT
        self.game.ground_image_bank = self.separate(pg.image.load(self.img_folder + GROUND_IMG).convert_alpha(), 50)

        #globu
        self.game.globu_img_bank = self.separate(pg.image.load(self.img_folder + GLOBU_IMG).convert_alpha(), 55)
        self.game.globu_img = self.game.globu_img_bank[0]
        self.game.globu_angry_img_bank = self.separate(pg.image.load(self.img_folder + GLOBU_IMG_ANGRY).convert_alpha(), 55)
        self.game.globu_bar = []
        self.game.globu_bar.append(pg.image.load(self.img_folder + GLOBU_LIFE))
        self.game.globu_bar.append(pg.image.load(self.img_folder + GLOBU_LIFE_EMPTY))



        #chest
        self.game.chest_image_bank = self.separate(pg.image.load(self.img_folder + CHEST_IMAGE).convert_alpha(), 51)

        #Gun Construct
        self.gold45_construct()
        self.wavax_construct()

        #ship
        self.game.ship_image_bank = []
        self.game.ship_image_bank.append(pg.image.load(self.ship_folder + SHIP_IMAGE).convert_alpha())
        self.game.ship_image_bank.append(pg.image.load(self.ship_folder + SHIP_IMAGE_EMPTY).convert_alpha())



        #wavegun
        #self.gold45_shot = pg.mixer.Sound(self.fire_sound_folder + GOLD45_BULLET_FIRESOUND)
        #self.gold45_shot.set_volume(0.15)
        #self.wavax_shot = pg.mixer.Sound(self.fire_sound_folder + WAVAX_BULLET_FIRESOUND)
        #self.wavax_shot.set_volume(0.01)

    def separate(self, img, w1, mult=1):
        w2 = img.get_width()
        h2 = img.get_height()
        timer = int(w2/w1)
        img_list = []
        for i in range(timer):
            img_list.append(img.subsurface(i*w1, 0, w1, h2))
            img_list[i] = pg.transform.scale(img_list[i], (int(mult*w1), int(mult*h2)))
            wc = int(img_list[i].get_width() / 1600 * WIDTH)
            hc = int(img_list[i].get_height() / 900 * HEIGHT)
            pg.transform.scale(img, (wc, hc))

        return img_list

    def wall_construct(self, img, mult=1):
        img_list = []
        for i in img[:3]: #3 * 4 = 12
            img_list.append(i)
            img_list.append(pg.transform.rotate(i, 270))
            img_list.append(pg.transform.rotate(i, 90))
            img_list.append(pg.transform.rotate(i, 180))
        img_list.append(img[3]) # +1

        return img_list

    def gold45_construct(self, mult=1):
        #LVL 1
        self.game.gold45_image_bank_lvl1 = list()
        self.game.gold45_image_bank_lvl1.append(pg.image.load(self.gold45_folder + GOLD45_LVL1_IMAGE).convert_alpha())
        self.game.gold45_image_bank_lvl1.append(pg.transform.flip(self.game.gold45_image_bank_lvl1[0], False, True))
        self.game.gold45_image_bank_lvl1.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL1_IMAGE).convert_alpha())
        #LVL 2
        self.game.gold45_image_bank_lvl2 = list()
        self.game.gold45_image_bank_lvl2.append(pg.image.load(self.gold45_folder + GOLD45_LVL2_IMAGE).convert_alpha())
        self.game.gold45_image_bank_lvl2.append(pg.transform.flip(self.game.gold45_image_bank_lvl2[0], False, True))
        self.game.gold45_image_bank_lvl2.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL2_IMAGE).convert_alpha())
        #LVL 3
        self.game.gold45_image_bank_lvl3 = list()
        self.game.gold45_image_bank_lvl3.append(pg.image.load(self.gold45_folder + GOLD45_LVL3_IMAGE).convert_alpha())
        self.game.gold45_image_bank_lvl3.append(pg.transform.flip(self.game.gold45_image_bank_lvl3[0], False, True))
        self.game.gold45_image_bank_lvl3.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL3_IMAGE).convert_alpha())
        #LVL 4
        self.game.gold45_image_bank_lvl4 = list()
        self.game.gold45_image_bank_lvl4.append(pg.image.load(self.gold45_folder + GOLD45_LVL4_IMAGE).convert_alpha())
        self.game.gold45_image_bank_lvl4.append(pg.transform.flip(self.game.gold45_image_bank_lvl4[0], False, True))
        self.game.gold45_image_bank_lvl4.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL4_IMAGE).convert_alpha())

    def wavax_construct(self, mult=1):
        #LVL 1
        self.game.wavax_image_bank_lvl1 = list()
        self.game.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_LVL1_IMAGE).convert_alpha())
        self.game.wavax_image_bank_lvl1.append(pg.transform.flip(self.game.wavax_image_bank_lvl1[0], False, True))
        self.game.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_LVL1_IMAGE_EMPTY).convert_alpha())
        self.game.wavax_image_bank_lvl1.append(pg.transform.flip(self.game.wavax_image_bank_lvl1[2], False, True))
        self.game.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL1_IMAGE).convert_alpha())
        #LVL 2
        self.game.wavax_image_bank_lvl2 = list()
        self.game.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_LVL2_IMAGE).convert_alpha())
        self.game.wavax_image_bank_lvl2.append(pg.transform.flip(self.game.wavax_image_bank_lvl2[0], False, True))
        self.game.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_LVL2_IMAGE_EMPTY).convert_alpha())
        self.game.wavax_image_bank_lvl2.append(pg.transform.flip(self.game.wavax_image_bank_lvl2[2], False, True))
        self.game.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL2_IMAGE).convert_alpha())
        #LVL 3
        self.game.wavax_image_bank_lvl3 = list()
        self.game.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_LVL3_IMAGE).convert_alpha())
        self.game.wavax_image_bank_lvl3.append(pg.transform.flip(self.game.wavax_image_bank_lvl3[0], False, True))
        self.game.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_LVL3_IMAGE_EMPTY).convert_alpha())
        self.game.wavax_image_bank_lvl3.append(pg.transform.flip(self.game.wavax_image_bank_lvl3[2], False, True))
        self.game.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL3_IMAGE).convert_alpha())
        #LVL 4
        self.game.wavax_image_bank_lvl4 = list()
        self.game.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_LVL4_IMAGE).convert_alpha())
        self.game.wavax_image_bank_lvl4.append(pg.transform.flip(self.game.wavax_image_bank_lvl4[0], False, True))
        self.game.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_LVL4_IMAGE_EMPTY).convert_alpha())
        self.game.wavax_image_bank_lvl4.append(pg.transform.flip(self.game.wavax_image_bank_lvl4[2], False, True))
        self.game.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL4_IMAGE).convert_alpha())
