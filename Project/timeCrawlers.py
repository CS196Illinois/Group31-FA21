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
    for projectile in player.projectiles:
        WIN.blit(projectile.image, (projectile.rect.x, projectile.rect.y))
        pygame.transform.rotate(projectile.image, projectile.ANGLE)
    pygame.display.update()

def updatePlayerStatus(player):
    if player.attackTimer > 0:
        player.attackTimer -= 1

def main(): # main function
    clock = pygame.time.Clock()
    p = player()
    run = True

    while run:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()
        mouseClicked = pygame.mouse.get_pressed()
        if mouseClicked[0]:
            p.attack(mx, my)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        p.handle_input()
        p.handle_projectiles()
        updatePlayerStatus(p)
        draw_window(p)

    pygame.quit()

if __name__ == "__main__": # call main function
    main()
