import pygame as pg
from settings import *
vec = pg.math.Vector2

def hit_rect_collision(one, two):
    #if one in two:
        #return False
    #else:
        return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, map):
        self.data = []
        with open(map, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.pos = vec(0, 0)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        self.pos.x = -target.rect.centerx + int(WIDTH / 2)
        self.pos.y = -target.rect.centery + int(HEIGHT / 2)

        #limit scrolling to the edge of the map
        self.pos.x = min(0, self.pos.x) #left
        self.pos.y = min(0,self.pos.y) #top
        self.pos.x = max(-(self.width - WIDTH), self.pos.x) #right
        self.pos.y = max(-(self.height - HEIGHT), self.pos.y) #bottom


        self.camera = pg.Rect(self.pos.x, self.pos.y, self.width, self.height)

        return(self.pos.x, self.pos.y)
