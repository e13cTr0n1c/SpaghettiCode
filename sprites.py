import pygame as pg
import math
from settings import *
from tilemap import hit_rect_collision
import random
vec = pg.math.Vector2

#global collision function
def collide_with_group(sprite, groups, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, groups, False)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.rect.width
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right
            sprite.vel.x = 0
            sprite.rect.x = sprite.pos.x

    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, groups, False)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.rect.height
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom
            sprite.vel.y = 0
            sprite.rect.y = sprite.pos.y

class Player(pg.sprite.Sprite):
    def __init__(self, game, camera, x, y,):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.camera = camera
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.mouse = vec(x, y)
        self.rot = 0
        self.angle = 0

        #checking for key inputs and moving player accordingly
    def get_inputs(self):
        self.vel = vec(0, 0)

        self.camx = self.game.camx
        self.camy = self.game.camy
        #checking mouse position to rotate player
        self.mousex, self.mousey = pg.mouse.get_pos()
        self.angle = math.atan2(self.mousex - (self.pos.x + self.camx), self.mousey - (self.pos.y + self.camy))
        self.angle = self.angle / 3.14159 * 180
        self.angle += 180
        #self.image = pg.transform.rotate(self.game.player_img, int(self.angle))


        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel.y = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel.x *= 0.7071
            self.vel.y *= 0.7071

    def update(self):
        self.get_inputs()
        self.image = pg.transform.rotate(self.game.player_img, int(self.angle))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        #if self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_group(self, self.game.walls,'x')
        self.hit_rect.centery = self.pos.y
        collide_with_group(self, self.game.walls,'y')
        self.rect.center + self.hit_rect.center

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.speed = random.randint(50, 200)
        self.game = game
        self.image = self.game.mob_img
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.rect.center = self.pos
        self.angle = 0

    def get_heading(self):
        self.angle = (self.game.player.hit_rect.center - self.pos).angle_to(vec(1, 0))

    def move(self, angle):
        self.angle = angle
        self.vel = vec(self.speed, 0).rotate(-self.angle)


    def update(self):
        self.get_heading()
        self.move(self.angle)
        self.image = pg.transform.rotate(self.game.mob_img, int(self.angle))
        self.pos.x += self.vel.x * self.game.dt
        self.pos.y += self.vel.y * self.game.dt
        self.rect.x = self.pos.x
        collide_with_group(self, self.game.walls, 'x')
        self.rect.y = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
