import pygame as pg
from settings import *

class Chest(pg.sprite.Sprite):
    def __init__(self, game, mobpos):
        self.groups = game.all_sprites, game.chests, game.collidewithplayer, game.collidewithmobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_bank = game.chest_image_bank
        self.image = self.image_bank[0]
        self.image_old = self.image
        self.pos = mobpos
        self.real_rect = self.image.get_rect()
        self.rect = self.real_rect
        self.real_rect.center = self.pos

    def update(self):
        self.real_rect.center = self.pos
