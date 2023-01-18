import pygame as pg
<<<<<<< HEAD
=======
vec = pg.math.Vector2
>>>>>>> 8b87b22 (six months of work)

#Defining colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (60, 60, 65)
LIGHTGREY = (100, 100, 100)
<<<<<<< HEAD
GREEN = (0, 255, 0)
=======
GREEN = (17, 100, 57)
>>>>>>> 8b87b22 (six months of work)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

#Game settings
pg.init()
RESOLUTION = pg.display.Info()

<<<<<<< HEAD
#Comment out the top two variable declarations for standard res, use them for screen res
=======
#Comment out the top two variable declarations for default res, use them for screen res
>>>>>>> 8b87b22 (six months of work)
WIDTH = RESOLUTION.current_w
HEIGHT = RESOLUTION.current_h
#WIDTH = 1000
#HEIGHT = 1000
FPS = 144
TITLE = "Madeleine McCann Search Party"
<<<<<<< HEAD
BGCOLOUR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#Player settings
PLAYER_SPEED = 400
PLAYER_IMG = 'mangun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 64, 64)

#Weapon settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 600
#Time before bullet despawns in ms
BULLET_LIFE = 1000

#Wall settings
WALL_IMG = 'tile_06.png'

#Enemy settings
MOB_SPEED_MIN = 250
MOB_SPEED_MAX = 450
MOB_IMG = 'zoimbie1_hold.png'
=======
THEME_MUSIC1 = 'themeMusic.mp3'
BG_IMG = 'background.png'
BGCOLOUR = GREEN
#Calculaing grid
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
#Player settings
PLAYER_SPEED = 400
PLAYER_IMG = 'playerSprite.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 64, 64)
#Weapon settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 700
#Time before bullet despawns in ms
BULLET_LIFE = 1200
BULLET_FIRERATE = 150
AVOID_RADIUS = 64
BARREL_OFFSET = vec(20, 20)
#KICKBACK = 150

#Wall settings
WALL_IMG = ['wall1.png','wall2.png', ]

OBJ_IMG = {
    '0' : 'woodHZ.png',
    '1' : 'woodVT.png',
    '2' : 'water.png'
}

FLOOR_IMG = {
    '0' : 'tile_01.png',
    '1' : 'tile_02.png',
    '2': 'tile_03.png',
    '3': 'tile_04.png'
}

#Enemy settings
MOB_SPEED_MIN = 400
MOB_SPEED_MAX = 800
MOB_IMG = ['zombieSprite.png', 'zombieSprite2.png']
>>>>>>> 8b87b22 (six months of work)
MOB_HIT_RECT = pg.Rect(0, 0, 65, 65)
