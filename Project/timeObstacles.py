import pygame
import os
from timeConfig import *
from timeBullet import Bullet
from timeSlash import Slash
from timePlayer import Player
from timeEnemy import Enemy

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.x = x
        self.y = y

        self.update_time = pygame.time.get_ticks()
        self.obstacle_list = []
        for i in range(12, 15):
            img = pygame.image.load(f'Project/assets/tile/{i}.png').convert_alpha()
            self.obstacle_list.append(img)
        self.image = self.obstacle_list[type]
        self.rect = self.image.get_rect()


    def draw_obstacle(self, screen):
        screen.blit(self.obstacle_list[self.type], (self.x, self.y))
