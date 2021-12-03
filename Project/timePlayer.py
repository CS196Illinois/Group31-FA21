import pygame
import os
from timeConfig import *
from timeBullet import Bullet
from timeSlash import Slash
from timeSniperBullet import sniperBullet
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.health = 100
        self.max_health = self.health

        #self.touchDoor = false
        self.level = 0

        self.equippedWeapon = "slash"
        self.shoot_cooldown = 0
        self.slash_cooldown = 0
        self.direction = 1
        self.flip = False

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        self.knockback_cooldown = 0

        #load all images for the players
        animation_types = ['idle', 'run', 'death']
        for animation in animation_types:
            #reset temporary list of images
            temp_list = []
            #count number of files in the folder
            num_of_frames = len(os.listdir(f'Project/assets/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'Project/assets/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, screen, enemy):
        self.update_animation()
        self.check_alive()
        self.healthbar(screen)
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.slash_cooldown > 0:
            self.slash_cooldown -= 1
        self.knockback(enemy)

    def move(self, moving_left, moving_right, moving_up, moving_down):
        #reset movement variables
        dx, dy = 0, 0

        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def knockback(self, enemy):
        if self.alive and enemy.alive:
            if self.rect.colliderect(enemy.rect):
                self.health -= 10
                self.knockback_cooldown = 15

        if self.knockback_cooldown > 0:
            self.knockback_cooldown -= 1
        if (self.rect.x-enemy.rect.x) > 0:
            self.rect.x += self.knockback_cooldown
        else:
            self.rect.x -= self.knockback_cooldown
        if (self.rect.y-enemy.rect.y) > 0:
            self.rect.y += self.knockback_cooldown
        else:
            self.rect.y -= self.knockback_cooldown

    def shootShotgun(self, mouse_x, mouse_y):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            for i in range(-2, 3):
                bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), \
                    self.rect.centery, mouse_x, mouse_y)
                bullet.shotgunBullet = True
                bullet.angle += (math.pi / 12) * i
                bullet_group.add(bullet)

    def shootSniper(self, mouse_x, mouse_y):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 60
            bullet = sniperBullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), \
                self.rect.centery, mouse_x, mouse_y)
            sniperbullet_group.add(bullet)

    def slash(self, mouse_x, mouse_y):
        if self.slash_cooldown == 0:
            self.slash_cooldown = 40
            slash = Slash(self.rect.centerx, self.rect.centery, mouse_x, mouse_y)
            slash_group.add(slash)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.rect.x, self.rect.y + self.image.get_height()+10, self.image.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.rect.x, self.rect.y + self.image.get_height()+10, self.image.get_width() * (self.health/self.max_health), 10))

    def update_animation(self):
        #update animation
        ANIMATION_COOLDOWN = 100
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(2)

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
