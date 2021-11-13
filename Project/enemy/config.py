import pygame

pygame.init()

WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("font/Pixeltype.ttf", 50)

sphere_group = pygame.sprite.Group()