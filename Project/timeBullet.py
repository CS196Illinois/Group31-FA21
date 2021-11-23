import pygame
import math
from timeConfig import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.image = pygame.transform.rotozoom(pygame.image.load('assets/icons/bullet.png'), -math.degrees(math.atan2(mouse_y - y, mouse_x - x)), 1)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        pygame.transform.rotozoom(self.image, self.angle, 1)
    
    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, x, y, xdir, ydir):
#         pygame.sprite.Sprite.__init__(self)
#         self.speed = 10
#         self.image = pygame.image.load('assets/icons/bullet.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.xdir, self.ydir = xdir, ydir

#     def update(self):
#         #move bullet
#         self.rect.x += (self.xdir * self.speed)
#         self.rect.y += (self.ydir * self.speed)
#         #check if bullet has gone off screen
#         if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
#             self.kill()