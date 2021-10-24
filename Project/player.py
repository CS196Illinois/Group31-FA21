import pygame

class player(pygame.sprite.Sprite):

    def __init__(self): #
        super().__init__()
        self.image = pygame.image.load("C:/Users/benja/github/Group31-FA21/Project/temporaryPlayerSprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.VELOCITY = 8
        self.DIRECTION = "RIGHT"

    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.VELOCITY
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.VELOCITY
        if keys_pressed[pygame.K_s]:
            self.rect.y += self.VELOCITY
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.VELOCITY
