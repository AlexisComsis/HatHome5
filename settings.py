import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (70, 70, 70)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 255, 255)
BLUE = (0, 35, 255)
PURPLE = (208, 0, 255)

# Game Settings
WIDTH = 1600
HEIGHT = 900
DIAGONAL = HEIGHT / WIDTH  #équation haut gauche bas droite : WIDTH x = HEIGHT y on calcul lautre avec
FPS = 60
TITLE = "HatHome"
BGCOLOR = BLACK

TILESIZE = 50
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = '\Wall.png'
GROUND_IMG = '\Ground.png'
MUSIC = '\\inquietant.mp3'

# ship
SHIP_IMAGE = '\Ship.png'
SHIP_IMAGE_EMPTY = '\Ship_empty.png'

# Player
PLAYER_SPEED = 400
PLAYER_BANK_IMG_UP = '\SpritePlayer_Down.png'
PLAYER_BANK_IMG_DOWN = '\SpritePlayer_Up.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 78, 96)
INVINCIBILITY_TIME = 50
PLAYER_LIFE = '\Life.png'
PLAYER_LIFE_EMPTY = '\Life_empty.png'
PLAYER_STAMINA = '\Stamina.png'
PLAYER_STAMINA_EMPTY = '\Stamina_empty.png'
# Mob
GLOBU_IMG = '\GlobuzarSprite.png'
GLOBU_IMG_ANGRY = '\GlobuzarSpriteAngry.png'
GLOBU_SPEED = 1000
GLOBU_HIT_RECT = pg.Rect(0, 0, 52, 100)
GLOBU_DROPCHEST = 0.01 #(4+1 chance / 100 car le 0 compt)
GLOBU_RANGE_B_PLAYER = 20
GLOBU_LIFE = '\Globu_life.png'
GLOBU_LIFE_EMPTY = '\Globu_life_empty.png'

# [Weapons]

#Gold45
#LVL 1
GOLD45_LVL1_IMAGE = '\Gold45.1.png'
GOLD45_BULLET_LVL1_IMAGE = '\Gold45_bullet.1.png'
GOLD45_LVL_IMAGE_TRUE = '\Gold45.1.True.png'
#LVL 2
GOLD45_LVL2_IMAGE = '\Gold45.2.png'
GOLD45_BULLET_LVL2_IMAGE = '\Gold45_bullet.2.png'
GOLD45_LVL2_ACTIVATE_IMAGE = '\Gold45_bullet.2_activate.png'
#LVL 3
GOLD45_LVL3_IMAGE = '\Gold45.3.png'
GOLD45_BULLET_LVL3_IMAGE = '\Gold45_bullet.3.png'
#LVL 4
GOLD45_LVL4_IMAGE = '\Gold45.4.png'
GOLD45_BULLET_LVL4_IMAGE = '\Gold45_bullet.4.png'

GOLD45_BULLET_IMAGE = '\Handgun_Bullet.png'
GOLD45_IMAGE = '\Gold.png'
GOLD45_DISTANCE = 30
GOLD45_LVL1_BULLET_SPEED = 70
GOLD45_LVL2_BULLET_SPEED = 10
GOLD45_BULLET_LIFETIME = 100000
GOLD45_BULLET_FIRECOOLDOWN = 500  #valeur plus élevé --> tirs plus espacés
GOLD45_BULLET_SHARP_FIRECOOLDOWN = 1000
GOLD45_BULLET_FIRESOUND = '\Gold45_shot.wav'
GOLD45_DAMAGE = 50
GOLD45_SHARP_DAMAGE = 80


#Wavax
#LVL 1
WAVAX_LVL1_IMAGE = '\Wavax.1.png'
WAVAX_LVL1_IMAGE_EMPTY = '\Wavax.1.empty.png'
WAVAX_BULLET_LVL1_IMAGE = '\Wavax_bullet.1.png'

#LVL 2
WAVAX_LVL2_IMAGE = '\Wavax.2.png'
WAVAX_LVL2_IMAGE_EMPTY = '\Wavax.2.empty.png'
WAVAX_BULLET_LVL2_IMAGE = '\Wavax_bullet.2.png'

#LVL 3
WAVAX_LVL3_IMAGE = '\Wavax.3.png'
WAVAX_LVL3_IMAGE_EMPTY = '\Wavax.3.empty.png'
WAVAX_BULLET_LVL3_IMAGE = '\Wavax_bullet.3.png'

#LVL 4
WAVAX_LVL4_IMAGE = '\Wavax.4.png'
WAVAX_LVL4_IMAGE_EMPTY = '\Wavax.4.empty.png'
WAVAX_BULLET_LVL4_IMAGE = '\Wavax_bullet.4.png'



WAVAX_BULLET_IMAGE = '\Wavegun_Bullet.png'
WAVAX_IMAGE = '\Wavegun.png'
WAVAX_DISTANCE = 40
WAVAX_BULLET_SPEED = 40
WAVAX_BULLET_LIFETIME = 100000
WAVAX_BULLET_FIRECOOLDOWN = 10  #valeur plus élevé --> tirs plus espacés
WAVAX_BULLET_FIRESOUND = '\Gold45_shot.wav'
WAVAX_DAMAGE = 2.5

#Chest
CHEST_IMAGE = '\Chest.png'

# Map
MAP = 'map.txt'



'''
    def wall_construct(self, img, mult=1):
        img_list = []
        for i in img[:3]: #3 * 4 = 12
            img_list.append(i)
            img_list.append(pg.transform.flip(i, False, True))
            iside = pg.transform.rotate(i, 90)
            img_list.append(iside)
            img_list.append(pg.transform.flip(iside, True, False))
            print(len(img_list))
        img_list.append(img[3]) # +1
        print(len(img_list))

        return img_list
'''
