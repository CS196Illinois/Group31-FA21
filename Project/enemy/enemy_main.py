import pygame
from config import *
from Enemy import Enemy

pygame.init()
pygame.display.set_caption("time crawlers")

BG = (155, 155, 155)

def draw_bg():
    WIN.fill(BG)

fly = Enemy("fly", 400, 400, 1, 5)

def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False  
    shoot = False

    while running:
        draw_bg()

        fly.update()
        fly.draw()
        fly.move(moving_left, moving_right, moving_up, moving_down)

        sphere_group.update()
        sphere_group.draw(WIN)

        if shoot:
            fly.shoot()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_w:
                    moving_up = True
                if event.key == pygame.K_s:
                    moving_down = True
                if event.key == pygame.K_SPACE:
                    shoot = True
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False
                if event.key == pygame.K_SPACE:
                    shoot = False
        
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()