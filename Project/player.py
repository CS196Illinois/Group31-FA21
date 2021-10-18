import pygame

class player(pygame.sprite.Sprite):

    def __init__(self): #
        super().__init__()
        self.image = pygame.image.load("temporaryPlayerSprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.VELOCITY = 5
        self.DIRECTION = "RIGHT"

    def move():
        keys_pressed = pygame.key.get_pressed()
