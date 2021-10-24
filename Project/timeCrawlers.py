import pygame
from player import player

# constants
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Crawlers")

FPS = 60

WHITE = (255, 255, 255)

def draw_window(player): # draw and update the window
    WIN.fill(WHITE)
    WIN.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.update()

def main(): # main function
    clock = pygame.time.Clock()
    p = player()
    run = True

    while run:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                p.attack()

        p.handle_movement()
        draw_window(p)

    pygame.quit()

if __name__ == "__main__": # call main function
    main()
