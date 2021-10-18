import pygame
from Player import player

# constants
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Crawlers")

WHITE = (255, 255, 255)

def draw_window(player): # draw and update the window
    WIN.fill(WHITE)
    WIN.blit(player, (player.x, player.y))
    pygame.display.update()

def main(): # main function
    p = player()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(p)

    pygame.quit()

if __name__ == "__main__": # call main function
    main()
