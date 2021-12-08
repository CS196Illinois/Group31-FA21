import pygame
from timeConfig import *

class sniperItem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Project/assets/icons/sniper.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, player):
        pickedUp = pygame.sprite.collide_rect(self, player)

        if pickedUp:
            player.ownedWeapons.append("sniper")
            item_group.remove(self)
            self.kill()
