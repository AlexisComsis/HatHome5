import pygame as pg
from settings import *

def Gold45_bank_construct(g):
    #LVL 1
    g.image_bank_lvl1 = list()
    g.image_bank_lvl1.append(pg.image.load(g.img_folder + GOLD45_LVL1_IMAGE).convert_alpha())
    g.image_bank_lvl1.append(pg.transform.flip(g.image_bank_lvl1[0], False, True))
    g.image_bank_lvl1.append(pg.image.load(g.img_folder + GOLD45_BULLET_LVL1_IMAGE).convert_alpha())
    #LVL 2
    g.image_bank_lvl2 = list()
    g.image_bank_lvl2.append(pg.image.load(g.img_folder + GOLD45_LVL2_IMAGE).convert_alpha())
    g.image_bank_lvl2.append(pg.transform.flip(g.image_bank_lvl1[0], False, True))
    g.image_bank_lvl2.append(pg.image.load(g.img_folder + GOLD45_BULLET_LVL2_IMAGE).convert_alpha())
    #LVL 3
    g.image_bank_lvl3 = list()
    g.image_bank_lvl3.append(pg.image.load(g.img_folder + GOLD45_LVL3_IMAGE).convert_alpha())
    g.image_bank_lvl3.append(pg.transform.flip(g.image_bank_lvl1[0], False, True))
    g.image_bank_lvl3.append(pg.image.load(g.img_folder + GOLD45_BULLET_LVL3_IMAGE).convert_alpha())
    #LVL 4
    g.image_bank_lvl4 = list()
    g.image_bank_lvl4.append(pg.image.load(g.img_folder + GOLD45_LVL4_IMAGE).convert_alpha())
    g.image_bank_lvl4.append(pg.transform.flip(g.image_bank_lvl1[0], False, True))
    g.image_bank_lvl4.append(pg.image.load(g.img_folder + GOLD45_BULLET_LVL4_IMAGE).convert_alpha())
