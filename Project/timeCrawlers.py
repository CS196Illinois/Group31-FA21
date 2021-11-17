import pygame

import os
import math
import random
from timePlayer import Player
from timeEnemy import Enemy
from timeChaser import Chaser
from timeConfig import *

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = int(SCREEN_WIDTH * 5/9)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('time crawler')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = False
slash = False

#define colours
BG = (155, 155, 155)
RED = (255, 0, 0)

def draw_bg():
    screen.fill(BG)
    # pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Soldier(pygame.sprite.Sprite):
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
            num_of_frames = len(os.listdir(f'assets/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.update_animation()
        self.check_alive()
        self.healthbar(screen)
        #update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.slash_cooldown > 0:
            self.slash_cooldown -= 1

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

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20

            for i in range (0, 8):
                randomX = random.randrange(-40, 40)
                randomY = random.randrange(-40 , 40)
                bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), \
                    self.rect.centery, mouse_x + randomX, mouse_y + randomY)
                bullet_group.add(bullet)

    def slash(self):
        if self.slash_cooldown == 0:
            self.slash_cooldown = 20
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

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

    def update(self):
        #move bullet
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        #check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.y < -50 or \
            self.rect.y > SCREEN_HEIGHT:
            self.kill()

        #check collision with characters
        # if pygame.sprite.spritecollide(player, bullet_group, False):
        #     if player.alive:
        #         player.health -= 5
        #         self.kill()
        if pygame.sprite.spritecollide(enemy, bullet_group, False):
            if enemy.alive:
                enemy.health -= 25
                self.kill()

class Slash(pygame.sprite.Sprite):
    def __init__(self, x, y, mouse_x, mouse_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.angle = math.atan2(y - mouse_y, x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        self.image = pygame.transform.rotozoom(slash_img, -math.degrees(math.atan2(mouse_y - y, mouse_x - x)), 1)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

        pygame.transform.rotozoom(self.image, self.angle, 1)

    def update(self):
        self.rect.x -= int(self.x_vel)
        self.rect.y -= int(self.y_vel)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.y < -50 or \
            self.rect.y > SCREEN_HEIGHT:
            self.kill()
        if pygame.sprite.spritecollide(enemy, slash_group, False):
            if enemy.alive:
                enemy.health -= 40
                self.kill()


#create sprite groups
bullet_group = pygame.sprite.Group()
slash_group = pygame.sprite.Group()

player = Player('player', 200, 200, 2, 5)
chaser = Chaser('enemy', 400, 200, 2, 1)

run = True
while run:
    clock.tick(FPS)

    draw_bg()

    chaser.update(screen, player)
    chaser.draw(screen)
    player.update(screen, chaser)
    player.draw(screen)

    #update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)

    slash_group.update()
    slash_group.draw(screen)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    #update player actions
    if player.alive:
        #shoot bullets
        if shoot:
            player.shoot(mouse_x, mouse_y)
        elif slash:
            player.slash(mouse_x, mouse_y)

        if moving_left or moving_right or moving_up or moving_down:
            player.update_action(1)#1: run
        else:
            player.update_action(0)#0: idle
        player.move(moving_left, moving_right, moving_up, moving_down)

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

            if event.key == pygame.K_1:
                player.equippedWeapon = "slash"
            if event.key == pygame.K_2:
                player.equippedWeapon = "shotgun"
            if event.key == pygame.K_3:
                player.equippedWeapon = "sniper"

            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                print(player.equippedWeapon)
                if player.equippedWeapon == "slash":
                    slash = True
                if player.equippedWeapon == "shotgun":
                    shoot = True

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:

                slash = False
                shoot = False

    pygame.display.update()

pygame.quit()

# import pygame
# from player import player

# # constants
# WIDTH, HEIGHT = (900, 500)
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Time Crawlers")

# FPS = 60

# WHITE = (255, 255, 255)

# def draw_window(player): # draw and update the window
#     WIN.fill(WHITE)
#     WIN.blit(player.image, (player.rect.x, player.rect.y))
#     for projectile in player.projectiles:
#         WIN.blit(projectile.image, (projectile.rect.x, projectile.rect.y))
#         pygame.transform.rotate(projectile.image, projectile.ANGLE)
#     pygame.display.update()

# def updatePlayerStatus(player):
#     if player.attackTimer > 0:
#         player.attackTimer -= 1

# def main(): # main function
#     clock = pygame.time.Clock()
#     p = player()
#     run = True

#     while run:
#         clock.tick(FPS)
#         mx, my = pygame.mouse.get_pos()
#         mouseClicked = pygame.mouse.get_pressed()
#         if mouseClicked[0]:
#             p.attack(mx, my)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False


#         p.handle_input()
#         p.handle_projectiles()
#         updatePlayerStatus(p)
#         draw_window(p)

#     pygame.quit()

# if __name__ == "__main__": # call main function
#     main()
