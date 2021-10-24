import pygame
import os
from Sphere import Sphere
from config import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.scale = scale
        self.speed = speed
        
        self.shoot_cooldown = 0
        self.direction = 1
        self.flip = False
    
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ["Idle"]
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f"assets/{self.char_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"assets/{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.update_animation()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def move(self, moving_left, moving_right, moving_up, moving_down):
        dx, dy = 0, 0

        if moving_left:
            dx = -self.speed
            self.flip = False
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = True
            self.direction = 1
        if moving_up:
            dy = -self.speed
        if moving_down:
            dy = self.speed
        
        self.rect.x += dx
        self.rect.y += dy
    
    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            sphere = Sphere(self.rect.centerx, self.rect.centery, self.direction)
            sphere_group.add(sphere)

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def draw(self):
        WIN.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)