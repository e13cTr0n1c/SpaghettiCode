import pygame as pg

#Defining colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (60, 60, 65)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

#Game settings
pg.init()
RESOLUTION = pg.display.Info()

#Comment out the top two variable declarations for standard res, use them for screen res
WIDTH = RESOLUTION.current_w
HEIGHT = RESOLUTION.current_h
#WIDTH = 1000
#HEIGHT = 1000
FPS = 144
TITLE = "Madeleine McCann Search Party"
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
MOB_HIT_RECT = pg.Rect(0, 0, 65, 65)
