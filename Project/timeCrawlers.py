import pygame
from timePlayer import Player
from timeEnemy import Enemy
from timeChaser import Chaser
from timeSniper import Sniper
from timeGiant import Giant
from timeWall import Wall
from timeObstacles import Obstacle
from sniperPickup import sniperItem
from shotgunPickup import shotgunItem
from medkit import medkit
from ragePowerup import ragePowerup
from timeConfig import *

pygame.init()

bg = pygame.image.load('Project/assets/tile/bg1.png')

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
shootShotgun = False
shootSniper = False
slash = False
slowingTime = False

#define colours
#BG = (155, 155, 155)
RED = (255, 0, 0)

def draw_bg():
    #screen.fill(BG)
    for i in range(3):
        a = i * 200
        for j in range(5):
            b = j * 200
            screen.blit(bg, (b,a))

walls_list = []
for i in range(30):
    a = i * 30
    wall = Wall(1, a, 470)
    walls_list.append(wall)

    wall = Wall(1, 0, a)
    walls_list.append(wall)

    wall = Wall(1, 870, a)
    walls_list.append(wall)

    wall = Wall(0, a, 0)
    walls_list.append(wall)

#indices: crate = 0, rock = 1,
obstacles_list = []
obstacles_list.append(Obstacle(0, 10, 100))
obstacles_list.append(Obstacle(1, 500, 30))
obstacles_list.append(Obstacle(2, 60, 700))



player = Player('player', 200, 200, 2, 5)
sniper = sniperItem(400, 200)
shotgun = shotgunItem(400, 300)
medkit = medkit(400, 400)
ragePowerup = ragePowerup(400, 100)
item_group.add(shotgun)
item_group.add(sniper)
item_group.add(medkit)
item_group.add(ragePowerup)

enemy_group.add(Chaser('enemy', 650, 200, 2, 2))
enemy_group.add(Sniper('enemy', 700, 200, 2, 2))
enemy_group.add(Giant('enemy', 600, 200, 4, 1))

# list of groups not pygame
# invincibility cooldown
enemy_list = []
enemy_list.append(Chaser('enemy', 650, 200, 2, 2))
enemy_list.append(Sniper('enemy', 700, 200, 2, 2))
enemy_list.append(Giant('enemy', 600, 200, 4, 1))
enemy_count = 0

run = True
while run:
    clock.tick(FPS)

    draw_bg()
    for i in walls_list:
        i.draw_wall(screen)
    #wall.draw_wall(screen)
    wall.draw_door(screen)

    for i in obstacles_list:
        i.draw_obstacle(screen)

    for enemy in enemy_list:
        enemy.update(screen, player)
        enemy.draw(screen)
        enemy_count += enemy.alive
        player.update(screen, enemy)
    # all the enemies are dead
    if (enemy_count == 0):
        print("clear")
    enemy_count = 0

    # for enemy in enemy_group.sprites():
    #     enemy.update(screen, player)
    #     enemy.draw(screen)
    #     if (not enemy.alive):
    #         enemy_group.remove(enemy)

    player.draw(screen)

    item_group.update(player)
    item_group.draw(screen)

    #update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)

    ebullet_group.update()
    ebullet_group.draw(screen)

    sniperbullet_group.update()
    sniperbullet_group.draw(screen)
    for sniperbullet in sniperbullet_group:
        sniperbullet.tracers.update()
        sniperbullet.tracers.draw(screen)

    slash_group.update()
    slash_group.draw(screen)

    projectiles = pygame.sprite.Group()
    projectiles.add(bullet_group.sprites())
    projectiles.add(slash_group.sprites())
    projectiles.add(sniperbullet_group.sprites())

    mouse_x, mouse_y = pygame.mouse.get_pos()

    #update player actions
    if player.alive:
        # bullets
        if shootShotgun:
            player.shootShotgun(mouse_x, mouse_y)
        elif shootSniper:
            player.shootSniper(mouse_x, mouse_y)
        elif slash:
            player.slash(mouse_x, mouse_y)

        if slowingTime:
            if player.timeCharge <= 0:
                slowingTime = False
            player.timeCharge -= 2
            FPS = 25
        else:
            if player.timeCharge < player.maxTimeCharge:
                player.timeCharge += .25
            FPS = 60
            #player.slowTime(enemy_group, projectiles)


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
            if event.key == pygame.K_SPACE and player.timeCharge >= 40:
                if (slowingTime == False):
                    slowingTime = True
                else:
                    slowingTime = False
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_1:
                player.equippedWeapon = "slash"
            if event.key == pygame.K_2 and "shotgun" in player.ownedWeapons:
                player.equippedWeapon = "shotgun"
            if event.key == pygame.K_3 and "sniper" in player.ownedWeapons:
                player.equippedWeapon = "sniper"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if player.equippedWeapon == "slash":
                    slash = True
                if player.equippedWeapon == "shotgun":
                    shootShotgun = True
                if player.equippedWeapon == "sniper":
                    shootSniper = True


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
                shootShotgun = False
                shootSniper = False

    pygame.display.update()

pygame.quit()
