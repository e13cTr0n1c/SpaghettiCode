import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        #RESOLUTION = pg.display.Info()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        pg.mixer.init()

        # Load audio file
        pg.mixer.music.load('themeMusic1.mp3')

        print("music started playing....")

        # Set preferred volume
        #mixer.music.set_volume(0.2)

        # Play the music
        pg.mixer.music.play()
        self.camx, self.camy = 0, 0

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'assets')
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.tilewidth = self.map.tilewidth
        self.tileheight = self.map.tileheight
        self.bg = pg.image.load(path.join(img_folder, BG_IMG)).convert_alpha()
        self.bg = pg.transform.scale(self.bg, (TILESIZE ** 2, TILESIZE **2))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img = pg.transform.scale(self.player_img, (TILESIZE, TILESIZE))
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        #self.bullet_img = pg.transform.scale(self.bullet_img, (TILESIZE, TILESIZE))
        self.mob_img = [pg.transform.scale(pg.image.load(path.join(img_folder, item)).convert_alpha(),(TILESIZE, TILESIZE)) for item in MOB_IMG]
        self.wall_img = [ pg.transform.scale(pg.image.load(path.join(img_folder, item)).convert_alpha(), (TILESIZE, TILESIZE)) for item in WALL_IMG]
        self.obj_img = [ pg.transform.scale(pg.image.load(path.join(img_folder, item)).convert_alpha(), (TILESIZE, TILESIZE)) for  item in OBJ_IMG.values()]
        self.floor_img = [pg.transform.scale(pg.image.load(path.join(img_folder, item)).convert_alpha(), (TILESIZE, TILESIZE)) for  item in FLOOR_IMG.values()]
        #self.theme_msc = pg.AUDIO_S8.load(path.join(img_folder, THEME_MUSIC1))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.floors = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

        self.camera = Camera(self.map.width, self.map.height)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                 if tile.isspace():
                    Floor(self, col, row, None)
                 elif tile == '#':
                    Wall(self, col, row)
                 elif tile == 'P':
                    self.player = Player(self, self.camera, col, row)
                    Floor(self, col, row, None)
                 elif tile == 'E':
                    self.enemy = Enemy(self, col, row)
                    Floor(self, col, row, None)
                    #SpawnPoint()
                 else:
                    Object(self, col, row, tile)


    def run(self):
        # game loop - set self.playing = False to end the game
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
        # update portion of the game loop
        #self.camx, self.camy = self.camera.update(self.player)
        self.all_sprites.update()
        self.camx, self.camy = self.camera.update(self.player)
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.kill()
            self.enemy = Enemy(self, 25, 50)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        #self.screen.fill(BGCOLOUR)
        #self.screen.blit(self.bg, (0, 0))
        for sprite in self.floors:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.walls:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.mobs:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.bullets:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        #for floor in self.floors
        #self.screen.blit(.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events here
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
