import pygame as pg
from settings import *

class Menu:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.run = True
        menu.button = pg.sprite.Group()
        self.update()

    def update(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
            mouse = pg.mouse.get_pos()

            x = mouse[0]
            y = mouse[1]


menu = Menu()

class Button(pg.sprite.Sprite):
    def __init__(self, img_false, img_true, song, rect):
        self.groups = menu.button
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image_true = img_true
        self.image_false = img_false
        self.song = song
        self.rect = rect
    def update:
