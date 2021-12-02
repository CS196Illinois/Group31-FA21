import pygame
import math
from timeConfig import *
from timeBullet import Bullet
from tracer import Tracer

class sniperBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.image = pygame.transform.rotozoom(pygame.image.load('Project/assets/icons/bullet.png'), -math.degrees(math.atan2(mouse_y - y, mouse_x - x)), 1)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        self.tracers = pygame.sprite.Group()

        pygame.transform.rotozoom(self.image, self.angle, 1)

    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        tracer = Tracer(self.rect.x, self.rect.y, self)
        self.tracers.add(tracer)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
