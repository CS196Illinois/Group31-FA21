import pygame
import math
from timeConfig import *

class Tracer(pygame.sprite.Sprite):
    def __init__(self, x, y, Bullet):
        pygame.sprite.Sprite.__init__(self)
        self.parent = Bullet
        self.speed = 0
        self.angle = math.atan2(x - Bullet.mouse_y, x - Bullet.mouse_x)
        self.image = pygame.transform.rotozoom(pygame.image.load('Project/assets/icons/bullet.png'), \
            -math.degrees(math.atan2(Bullet.mouse_y - y, Bullet.mouse_x - x)), 1)
        self.rect = self.image.get_rect()
        self.rect.center = Bullet.rect.center
        pygame.transform.rotozoom(self.image, self.angle, 1)

    def update(self):
        if self.parent is None:
            self.kill()
