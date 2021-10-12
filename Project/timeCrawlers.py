import pygame

# constants
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Crawlers")

WHITE = (255, 255, 255)

def draw_window(): # draw and update the window
    WIN.fill(WHITE)
    pygame.display.update()

def main(): # main function
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__": # call main function
    main()
