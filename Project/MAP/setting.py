import pygame as pg
vec = pg.math.Vector2

#color settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

#screen, window, and game settings
WIDTH = 1024   #32 * 32
HEIGHT = 768   #32 * 24
FPS = 120
TITLE = "Map_test1_demo"
BGCOLOR = DARKGREY #backgroud color

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#image settings

WALL_IMG = 'tileGreen_39.png'

# Player settings
#PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob settings
"""
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
"""
