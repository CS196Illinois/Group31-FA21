import pygame
import os
import math

class slash(pygame.sprite.Sprite):
    def __init__(self, player, mx, my): #
        super().__init__()
        self.distance_x = mx - player.rect.x
        self.distance_y = my - player.rect.y
        self.ANGLE = math.atan2(self.distance_y, self.distance_x)
        self.image = pygame.image.load("temporarySlashSprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.VELOCITY = 8

    def update(self):
        self.rect.x += self.VELOCITY * math.cos(self.ANGLE)
        self.rect.y += self.VELOCITY * math.sin(self.ANGLE)
