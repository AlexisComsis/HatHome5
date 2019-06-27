import pygame as pg
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

            self.tilewidth = len(self.data[0])
            self.tileheight= len(self.data)
            self.width = self.tilewidth * TILESIZE
            self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self,entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):

        newx = int(WIDTH/2) - target.rect.center[0]
        newy = int(HEIGHT/2) - target.rect.center[1]
        self.camera = pg.Rect(newx, newy, self.width, self.height)
