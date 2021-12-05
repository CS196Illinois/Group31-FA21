import pygame
from timeConfig import *

class ragePowerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'Project/assets/icons/damageBoost.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, player):
        pickedUp = pygame.sprite.collide_rect(self, player)

        if pickedUp:
            player.isRaging = True
            item_group.remove(self)
            self.kill()
