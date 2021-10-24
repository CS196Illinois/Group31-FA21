import pygame
import os

class player(pygame.sprite.Sprite):

    def __init__(self): #
        super().__init__()
        self.image = pygame.image.load("temporaryPlayerSprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.VELOCITY = 8
        player.HEALTH = 3
        self.DIRECTION = "RIGHT"
        self.weapons = ["sword", "shotgun", "sniper"]
        self.equippedWeapon = "sword"

    def handle_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.VELOCITY
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.VELOCITY
        if keys_pressed[pygame.K_s]:
            self.rect.y += self.VELOCITY
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.VELOCITY

    def attack(self):
        print("hello")
