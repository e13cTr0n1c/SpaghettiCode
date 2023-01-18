import pygame as pg
import math
from settings import *
from tilemap import hit_rect_collision
import random
<<<<<<< HEAD
vec = pg.math.Vector2

#global collision function
def collide_with_group(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, hit_rect_collision)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, hit_rect_collision)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
=======
vec = pg.math.Vector2

#global collision function
def collide_with_group(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, hit_rect_collision)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, hit_rect_collision)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
>>>>>>> 8b87b22 (six months of work)


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
<<<<<<< HEAD
=======
        self.last_update = BULLET_FIRERATE
>>>>>>> 8b87b22 (six months of work)
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
<<<<<<< HEAD
        self.angle = math.atan2(self.mousex - (self.pos.x + self.camx), self.mousey - (self.pos.y + self.camy))
=======
        self.angle = math.atan2(self.mousex - (self.hit_rect.centerx + self.camx), self.mousey - (self.hit_rect.centery + self.camy))
>>>>>>> 8b87b22 (six months of work)
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
<<<<<<< HEAD
=======
        if keys[pg.K_SPACE]:
            now = pg.time.get_ticks()
            if now - self.last_update > BULLET_FIRERATE:
                self.last_update = now
                pos = self.pos - (BARREL_OFFSET.rotate(-self.angle+90))
                mouse_pos = vec(self.mousex, self.mousey)



                Bullet(self.game, pos, mouse_pos, self.angle)
                #self.vel = vec(-KICKBACK, 0).rotate(-self.rot)


>>>>>>> 8b87b22 (six months of work)

    def update(self):
        self.get_inputs()
        self.image = pg.transform.rotate(self.game.player_img, int(self.angle))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_group(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
<<<<<<< HEAD
        self.rect.center = self.hit_rect.center
        print(self.rect)

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, angle_to):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface
=======
        self.rect.center = self.hit_rect.center

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos, mouse_pos, rot):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.bullet_img
        self.image = pg.transform.rotate(self.image, rot)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.rect.center = pos
        self.angle = math.atan2(mouse_pos.x - (pos.x + game.camx), mouse_pos.y - (pos.y + game.camy))
        self.vel = vec(math.sin(self.angle),math.cos(self.angle)).normalize()*BULLET_SPEED
        self.spawn_time = pg.time.get_ticks()

#class Gun(pg.sprite.Sprite):

    #def __init__(self, player,):
        #self.groups = player.group_sprites,

    def update(self):
        self.pos += self.vel * self.game.dt
        self.rect.center = self.pos
        if pg.time.get_ticks() - self.spawn_time > BULLET_LIFE:
            self.kill()

        if pg.sprite.spritecollideany(self, self.game.walls):
            self.kill()


>>>>>>> 8b87b22 (six months of work)


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
<<<<<<< HEAD
        self.image = game.wall_img
=======
        self.random_wall = random.randint(0, len(MOB_IMG) - 1)
        self.image = game.wall_img[self.random_wall]
>>>>>>> 8b87b22 (six months of work)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

<<<<<<< HEAD
=======
class Object(pg.sprite.Sprite):
    def __init__(self, game, x, y, tile):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.tile = int(tile)
        self.image = game.obj_img[self.tile]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x ,y, tile):
        self.groups = game.all_sprites, game.floors
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        if tile:
            self.tile = int(tile)
            self.image = game.floor_img[self.tile]
        else:
            print('test')
            self.random_grass = random.randint(0, len(FLOOR_IMG) - 1)
            self.image = game.floor_img[self.random_grass]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class SpawnPoint(pg.sprite.Sprite):
    def __init__(self, game, x, y)

>>>>>>> 8b87b22 (six months of work)
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.speed = random.randint(MOB_SPEED_MIN, MOB_SPEED_MAX)
        self.game = game
<<<<<<< HEAD
        self.image = self.game.mob_img
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.angle = 0
=======
        self.random_mob = random.randint(0, len(MOB_IMG)-1)
        self.image = game.mob_img[self.random_mob]
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.angle = 90
>>>>>>> 8b87b22 (six months of work)

    def get_heading(self):
        self.angle = (self.game.player.pos - self.pos).angle_to(vec(1, 0))

    def move(self, angle):
<<<<<<< HEAD
        self.angle = angle
        self.vel = vec(self.speed, 0).rotate(-self.angle)
        self.image = pg.transform.rotate(self.game.mob_img, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(self.speed , 0).rotate(-self.angle)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 10 * self.acc #* self.game.dt ** 2
        self.rect.x = self.pos.x
        collide_with_group(self, self.game.walls, 'x')
        self.rect.y = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
=======

        self.vel = vec(self.speed, 0).rotate(-self.angle)
        self.image = pg.transform.rotate(self.game.mob_img, self.angle-90)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.acc = vec(self.speed , 0).rotate(-self.angle)
        self.acc += self.vel #* -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 10 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_group(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        self.avoid_mobs()

    def avoid_mobs(self):
        for mob in self.game.mobs:
            if mob != self:
                dist = self.pos - mob.pos
                #print(dist)
                if dist.length() < AVOID_RADIUS:
                    #if abs(self.vel.x) < 40 or abs(self.vel.y) < 40:
                    self.vel = dist

    #I will not include a healthbar show procedure as this will mean enemies will only display health bar once damaged.
    #def health_bar(self, damage):
>>>>>>> 8b87b22 (six months of work)


    def update(self):
        #self.get_heading()
<<<<<<< HEAD
        #self.move(self.angle)
        self.angle = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.game.mob_img, self.angle)
        # self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(self.speed, 0).rotate(-self.angle)
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        collide_with_group(self, self.game.walls, 'x')
        collide_with_group(self, self.game.mobs, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
        collide_with_group(self, self.game.mobs, 'y')
        self.rect.center = self.hit_rect.center
=======
        #self.move(self.angle)

        self.angle = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pg.transform.rotate(self.game.mob_img[self.random_mob], self.angle+90)
        # self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(self.speed, 0).rotate(-self.angle)
        self.avoid_mobs()
        self.acc += self.vel * -1
        self.vel += self.acc * self.game.dt
        self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        self.hit_rect.centerx = self.pos.x
        self.otherMobs = self.game.mobs
        #otherEnemies = self.game.mobs

        collide_with_group(self, self.game.walls, 'x')
        #collide_with_group(self, self.game.mobs, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_group(self, self.game.walls, 'y')
        #collide_with_group(self, self.game.mobs, 'y')
        self.rect.center = self.hit_rect.center
>>>>>>> 8b87b22 (six months of work)
