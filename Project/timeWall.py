import pygame
import os
from timeConfig import *
from timeBullet import Bullet
from timeSlash import Slash
from timePlayer import Player
from timeEnemy import Enemy

class Wall(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.x = x
        self.y = y

        self.update_time = pygame.time.get_ticks()

        self.wall_list = []
        self.wall_list.append(pygame.image.load(f'Project/assets/tile/7.png').convert_alpha())
        self.wall_list.append(pygame.image.load(f'Project/assets/tile/4.png').convert_alpha())
        self.image = self.wall_list[type]
        self.rect = self.image.get_rect()

        self.obstacle_list = []
        for i in range(12, 15):
            img = pygame.image.load(f'Project/assets/tile/{i}.png').convert_alpha()
            self.obstacle_list.append(img)

        self.door = pygame.image.load('Project/assets/tile/20.png')
        #load all images for the players
        #animation_types = ['Idle', 'Run', 'Death']
        # for animation in animation_types:
        #     #reset temporary list of images
        #     temp_list = []
        #     #count number of files in the folder
        #     num_of_frames = len(os.listdir(f'assets/{self.char_type}/{animation}'))
        #     for i in range(num_of_frames):
        #         img = pygame.image.load(f'assets/{self.char_type}/{animation}/{i}.png').convert_alpha()
        #         img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        #         temp_list.append(img)
        #     self.animation_list.append(temp_list)


    def update(self, screen):
        self.update_animation()

        hit_bullet = pygame.sprite.spritecollide(self, bullet_group, False)
        hit_slash = pygame.sprite.spritecollide(self, slash_group, False)

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

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


    def draw_wall(self, screen):
        screen.blit(self.wall_list[self.type], (self.x, self.y))


    def draw_door(self, screen):
        for i in range(1, 4):
            a = i * 30
            screen.blit(self.door, (900 - a, 210))
            screen.blit(self.door, (900 - a, 330))
