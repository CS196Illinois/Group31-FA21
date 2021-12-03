import pygame
import os
from timeConfig import *
from timeBullet import Bullet

class Sniper(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.health = 100
        self.max_health = self.health
        
        self.shoot_cooldown = 0
        self.slash_cooldown = 0
        self.direction = 1
        self.flip = False

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        #load all images for the players
        animation_types = ['Idle', 'Run', 'Death']
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

    def update(self, screen, player):
        self.update_animation()
        self.check_alive()
        self.healthbar(screen)
        self.move(player)
        self.shoot(player)

        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        hit_bullet = pygame.sprite.spritecollide(self, bullet_group, False)
        hit_sniperbullet = pygame.sprite.spritecollide(self, sniperbullet_group, False)
        hit_slash = pygame.sprite.spritecollide(self, slash_group, False)

        if hit_bullet:
            if self.alive:
                self.health -= 1
                bullet_group.remove(hit_bullet)
        if hit_sniperbullet:
            if self.alive:
                self.health -= 100
        if hit_slash:
            if self.alive:
                self.health -= 40
                slash_group.remove(hit_slash)

    def move(self, player):
        #reset movement variables
        dx, dy = (player.rect.x-self.rect.x), (player.rect.y-self.rect.y)

        if self.alive:
            if dx == 0 and dy == 0:
                self.update_action(0)
            if dx < 0:
                self.rect.x -= self.speed
                self.flip = True
                self.update_action(1)
            elif dx >= 1:
                self.rect.x += self.speed
                self.flip = False
                self.update_action(1)
            if dy < 0:
                self.rect.y -= self.speed
                self.update_action(1)
            elif dy >= 1:
                self.rect.y += self.speed
                self.update_action(1)
        else:
            self.update_action(2)

    def shoot(self, player):
        if self.alive:
            if self.shoot_cooldown == 0:
                self.shoot_cooldown = 120
                bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, player.rect.centerx, player.rect.centery)
                ebullet_group.add(bullet)
    
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