import pygame
from sys import exit

def obstacle_display(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            WIN.blit(fly_surf, obstacle_rect)
        
        return obstacle_list
    else:
        return []

# def collision(player, obstacles)

pygame.init()
WIDTH, HEIGHT = (900, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Time Crawlers")
test_font = pygame.font.Font("font/Pixeltype.ttf", 50) # bring font file, px

game_active = False

bg_surf = pygame.transform.scale(pygame.image.load("assets/bg.png").convert(), (WIDTH, HEIGHT))

fly_frame_1 = pygame.image.load("assets/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("assets/fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]
fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)

obstacle_rect_list = []

def main(): # main function
    running = True
    FPS = 60
    clock = pygame.time.Clock()
    game_active = False
    
    global obstacle_rect_list
    global fly_frame_index
    global fly_surf
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: 
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]
        
        if game_active:
            WIN.blit(bg_surf, (0, 0))
            if (len(obstacle_rect_list) == 0):
                obstacle_rect_list.append(fly_surf.get_rect(center=(WIDTH/2, HEIGHT/2)))
            else:
                print(obstacle_rect_list)

            # OBSTACLE DISPLAY
            obstacle_rect_list = obstacle_display(obstacle_rect_list)

        else: 
            WIN.blit(bg_surf, (0, 0))
            game_message = test_font.render("Press [Space] to spawn an enemy", False, (255, 255, 255))
            game_message_rect = game_message.get_rect(center=(WIDTH/2, HEIGHT/2))
            WIN.blit(game_message, game_message_rect)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__": # call main function
    main()