import pygame
from sys import exit
from random import choice

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == "fly":
            fly_1 = pygame.image.load("assets/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("assets/fly2.png").convert_alpha()
            self.frames = [fly_1, fly_2]

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT/2))

    def animation_state(self):
        self.animation_index += 0.1 
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
	
    def update(self):
        self.animation_state()
        # self.destroy()
    
    # def destroy(self):
    #     if condition:
    #         self.kill()

pygame.init()
pygame.display.set_caption("Time Crawlers")
game_active = False

WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.Font("font/Pixeltype.ttf", 50) # bring font file, px

bg_surf = pygame.transform.scale(pygame.image.load("assets/bg.png").convert(), (WIDTH, HEIGHT))
enemy_group = pygame.sprite.Group()

def main(): # main function
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    game_active = False
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
            
            if game_active:
                if (len(enemy_group) == 0):
                    enemy_group.add(Enemy(choice(["fly"])))

        if game_active:
            WIN.blit(bg_surf, (0, 0))            
            enemy_group.draw(WIN)
            enemy_group.update()
        else: 
            game_message = FONT.render("Press [Space] to spawn an enemy", False, (255, 255, 255))
            game_message_rect = game_message.get_rect(center=(WIDTH/2, HEIGHT/2))
            WIN.blit(game_message, game_message_rect)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__": # call main function
    main()