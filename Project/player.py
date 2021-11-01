import pygame
import os
from slash import slash

class player(pygame.sprite.Sprite):

    def __init__(self): #
        super().__init__()
        self.image = pygame.image.load("temporaryPlayerSprite.png")
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 300
        self.VELOCITY = 8
        player.HEALTH = 3
        self.equippedWeapon = "sword"
        self.swordCooldown = 20
        self.shotgunCooldown = 30
        self.sniperCooldown = 40
        self.attackTimer = 0
        self.projectiles = []

    def handle_input(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.VELOCITY
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.VELOCITY
        if keys_pressed[pygame.K_s]:
            self.rect.y += self.VELOCITY
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.VELOCITY

        if keys_pressed[pygame.K_1]:
            self.equippedWeapon = "sword"
        if keys_pressed[pygame.K_2]:
            self.equippedWeapon = "shotgun"
        if keys_pressed[pygame.K_3]:
            self.equippedWeapon = "sniper"

    def attack(self, mx, my):
        if self.attackTimer == 0:
            if self.equippedWeapon == "sword":
                self.attackTimer = self.swordCooldown
                s = slash(self, mx, my)
                self.projectiles.append(s)
            elif self.equippedWeapon == "shotgun":
                self.attackTimer = self.shotgunCooldown
            else:
                self.attackTimer = self.sniperCooldown

    def handle_projectiles(self):
        for projectile in self.projectiles:
            if projectile.rect.x < 0 or projectile.rect.x > 900 or projectile.rect.y < 0 or \
                    projectile.rect.y > 500:
                self.projectiles.remove(projectile)
            projectile.update()
