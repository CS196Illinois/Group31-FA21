import pygame
from config import *

class Sphere(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.image.load("assets/icons/sphere.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
    
    def update(self):
        self.rect.x += (self.direction * self.speed)
        
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()