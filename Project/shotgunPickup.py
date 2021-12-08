import pygame
from timeConfig import *

class shotgunItem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Project/assets/icons/shotgun.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, player):
        pickedUp = pygame.sprite.collide_rect(self, player)

        if pickedUp:
            player.ownedWeapons.append("shotgun")
            item_group.remove(self)
            self.kill()
