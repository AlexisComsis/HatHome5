import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *
#from gold45 import *
#from wavax import *


class Game:

    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
        pg.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT), pg.FULLSCREE)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(50, 100)
        self.load_data()


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
        self.gold45_image_bank_lvl1 = list()
        self.gold45_image_bank_lvl1.append(pg.image.load(self.gold45_folder + GOLD45_LVL1_IMAGE).convert_alpha())
        self.gold45_image_bank_lvl1.append(pg.transform.flip(self.gold45_image_bank_lvl1[0], False, True))
        self.gold45_image_bank_lvl1.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL1_IMAGE).convert_alpha())
        #LVL 2
        self.gold45_image_bank_lvl2 = list()
        self.gold45_image_bank_lvl2.append(pg.image.load(self.gold45_folder + GOLD45_LVL2_IMAGE).convert_alpha())
        self.gold45_image_bank_lvl2.append(pg.transform.flip(self.gold45_image_bank_lvl2[0], False, True))
        self.gold45_image_bank_lvl2.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL2_IMAGE).convert_alpha())
        #LVL 3
        self.gold45_image_bank_lvl3 = list()
        self.gold45_image_bank_lvl3.append(pg.image.load(self.gold45_folder + GOLD45_LVL3_IMAGE).convert_alpha())
        self.gold45_image_bank_lvl3.append(pg.transform.flip(self.gold45_image_bank_lvl3[0], False, True))
        self.gold45_image_bank_lvl3.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL3_IMAGE).convert_alpha())
        #LVL 4
        self.gold45_image_bank_lvl4 = list()
        self.gold45_image_bank_lvl4.append(pg.image.load(self.gold45_folder + GOLD45_LVL4_IMAGE).convert_alpha())
        self.gold45_image_bank_lvl4.append(pg.transform.flip(self.gold45_image_bank_lvl4[0], False, True))
        self.gold45_image_bank_lvl4.append(pg.image.load(self.gold45_folder + GOLD45_BULLET_LVL4_IMAGE).convert_alpha())

    def wavax_construct(self, mult=1):
        #LVL 1
        self.wavax_image_bank_lvl1 = list()
        self.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_LVL1_IMAGE).convert_alpha())
        self.wavax_image_bank_lvl1.append(pg.transform.flip(self.wavax_image_bank_lvl1[0], False, True))
        self.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_LVL1_IMAGE_EMPTY).convert_alpha())
        self.wavax_image_bank_lvl1.append(pg.transform.flip(self.wavax_image_bank_lvl1[2], False, True))
        self.wavax_image_bank_lvl1.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL1_IMAGE).convert_alpha())
        #LVL 2
        self.wavax_image_bank_lvl2 = list()
        self.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_LVL2_IMAGE).convert_alpha())
        self.wavax_image_bank_lvl2.append(pg.transform.flip(self.wavax_image_bank_lvl2[0], False, True))
        self.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_LVL2_IMAGE_EMPTY).convert_alpha())
        self.wavax_image_bank_lvl2.append(pg.transform.flip(self.wavax_image_bank_lvl2[2], False, True))
        self.wavax_image_bank_lvl2.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL2_IMAGE).convert_alpha())
        #LVL 3
        self.wavax_image_bank_lvl3 = list()
        self.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_LVL3_IMAGE).convert_alpha())
        self.wavax_image_bank_lvl3.append(pg.transform.flip(self.wavax_image_bank_lvl3[0], False, True))
        self.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_LVL3_IMAGE_EMPTY).convert_alpha())
        self.wavax_image_bank_lvl3.append(pg.transform.flip(self.wavax_image_bank_lvl3[2], False, True))
        self.wavax_image_bank_lvl3.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL3_IMAGE).convert_alpha())
        #LVL 4
        self.wavax_image_bank_lvl4 = list()
        self.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_LVL4_IMAGE).convert_alpha())
        self.wavax_image_bank_lvl4.append(pg.transform.flip(self.wavax_image_bank_lvl4[0], False, True))
        self.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_LVL4_IMAGE_EMPTY).convert_alpha())
        self.wavax_image_bank_lvl4.append(pg.transform.flip(self.wavax_image_bank_lvl4[2], False, True))
        self.wavax_image_bank_lvl4.append(pg.image.load(self.wavax_folder + WAVAX_BULLET_LVL4_IMAGE).convert_alpha())

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
        self.map = Map(path.join(self.game_folder, MAP))
        #self.music = pg.mixer.music.load(self.sound_folder + MUSIC)
        #pg.mixer.music.set_volume(1)
        #pg.mixer.music.play(-1)

        #player
        self.player_image_bank = self.separate(pg.image.load(self.img_folder + PLAYER_BANK_IMG).convert_alpha(), 78)

        #wall
        self.wall_image_bank = self.separate(pg.image.load(self.img_folder + WALL_IMG).convert_alpha(), 50) # LIST 4 ELEMENT
        self.wall_image_bank = self.wall_construct(self.wall_image_bank) #LIST 13 ELEMENT
        self.ground_image_bank = self.separate(pg.image.load(self.img_folder + GROUND_IMG).convert_alpha(), 50)

        #globu
        self.globu_img_bank = self.separate(pg.image.load(self.img_folder + GLOBU_IMG).convert_alpha(), 55)
        self.globu_img = self.globu_img_bank[0]

        #chest
        self.chest_image_bank = self.separate(pg.image.load(self.img_folder + CHEST_IMAGE).convert_alpha(), 51)

        #Gun Construct
        self.gold45_construct()
        self.wavax_construct()

        #ship
        self.ship_image_bank = self.separate(pg.image.load(self.ship_folder + SHIP_IMAGE).convert_alpha(), 200)


        #wavegun
        #self.gold45_shot = pg.mixer.Sound(self.fire_sound_folder + GOLD45_BULLET_FIRESOUND)
        #self.gold45_shot.set_volume(0.15)
        #self.wavax_shot = pg.mixer.Sound(self.fire_sound_folder + WAVAX_BULLET_FIRESOUND)
        #self.wavax_shot.set_volume(0.01)

    def new(self):
        #pg.mixer.music.play(-1)
        self.all_sprites = pg.sprite.Group()
        self.collidewithplayer = pg.sprite.Group()
        self.collidewithmobs = pg.sprite.Group()
        self.collidewithmobs2 = pg.sprite.Group()
        self.chests = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grounds = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.weapons = pg.sprite.Group()
        self.playersprite = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.bulletssharp = pg.sprite.Group()
        self.ships = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '.':#Ground
                    Ground(self, col, row)
                elif tile == 'T': #Top
                    Wall(self, col, row, 0)
                elif tile == 'R': #Bot
                    Wall(self, col, row, 1)
                elif tile == 'L': #left
                    Wall(self, col, row, 2)
                elif tile == 'B': #Right
                    Wall(self, col, row, 3)
                elif tile == '0': #TopL_ext
                    Wall(self, col, row, 4)
                elif tile == '1': #BotL_ext
                    Wall(self, col, row, 5)
                elif tile == '2': #BotL_ext
                    Wall(self, col, row, 6)
                elif tile == '3': #Bot_ext
                    Wall(self, col, row, 7)
                elif tile == '4':
                    Wall(self, col, row, 8)
                elif tile == '5':
                    Wall(self, col, row, 9)
                elif tile == '6':
                    Wall(self, col, row, 10)
                elif tile == '7':
                    Wall(self, col, row, 11)
                elif tile == '8':
                    Wall(self, col, row, 12)
                elif tile == '9':
                    Wall(self, col, row, 13)
                elif tile == 'G' or tile == 'P' or tile == 'S':
                    Ground(self, col, row)


        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    self.player = Player(self, col, row)
                    #self.weapon = Gold(self)
                elif tile == 'G':
                    Mob(self, col, row, 0)

                elif tile == 'S':
                    self.ship = Ship(self, col, row)



        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.mousepos = pg.mouse.get_pos()
        self.mousepos = vec(self.mousepos)
        self.mousex = self.mousepos[0]
        self.mousey = self.mousepos[1]
        self.all_sprites.update()
        self.camera.update(self.player)



    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.window, BLACK, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.window, BLACK, (0, y), (WIDTH, y))

    def draw(self):
        self.window.fill(BGCOLOR)
        #self.draw_grid()
        '''
        self.all_sprites = pg.sprite.Group()
        self.collidewithplayer = pg.sprite.Group()
        self.collidewithmobs = pg.sprite.Group()
        self.chests = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.grounds = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.playersprite = pg.sprite.Group()
        self.weapons = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.bulletssharp = pg.sprite.Group()
        '''
        for sprite in self.all_sprites:
                self.window.blit(sprite.image, self.camera.apply(sprite))





        Player.draw_player_health(self.window, 10, 10, self.player.life / self.player.max_life)
        Player.draw_player_stamina(self.window, 300, 10, self.player.stamina / self.player.max_stamina)

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
