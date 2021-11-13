import numpy as np
import math
import random
import pygame

pygame.init()
size, level, diff = 7, 4, 1
scale = 50
WIDTH, HEIGHT = int(size*scale*9/5), size*scale
screen = pygame.display.set_mode((WIDTH, HEIGHT + 75))
pygame.display.set_caption('map level generator')
clock = pygame.time.Clock()
FPS = 60

colors = [
    pygame.Color("#333333"), 
    pygame.Color("#69B34C"), 
    pygame.Color("#ACB334"), 
    pygame.Color("#FAB733"), 
    pygame.Color("#FF8E15"), 
    pygame.Color("#FF4E11"), 
    pygame.Color("#FF0D0D")
]

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#load button images
start_img = pygame.image.load('assets/gen_btn.png').convert_alpha()

#create button instances
start_button = Button(WIDTH*3/7, HEIGHT, start_img, 0.5)

def create_map(size, level, difficulty):
    init =  np.zeros((size, size))
    x, y = math.floor(size / 2), math.floor(size / 2)
    init[x, y] = 1
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for i in direction:
        init[x+i[0], y+i[1]] = 2

    curr_x, curr_y = np.where(init == 2)
    curr_check = []
    for i in range(len(curr_x)):
        curr_check.append([curr_x[i], curr_y[i]])
    
    curr_lvl = 3
    while (level >= curr_lvl):
        for j in range(difficulty):
            for i in range(len(curr_check)):
                rand = random.randint(0, 3)
                if (0 < curr_check[i][0]+direction[rand][0] < size and 0 < curr_check[i][1]+direction[rand][1] < size
                    and int(init[curr_check[i][0]+direction[rand][0], curr_check[i][1]+direction[rand][1]]) == 0):
                    init[curr_check[i][0]+direction[rand][0], curr_check[i][1]+direction[rand][1]] = curr_lvl
        curr_x, curr_y = np.where(init == curr_lvl)
        curr_check = []
        for i in range(len(curr_x)):
            curr_check.append([curr_x[i], curr_y[i]])
        curr_lvl += 1
    
    return init

def draw_map():
    for i in range(len(map)):
        for j in range(len(map[i])):
            pygame.draw.rect(screen, colors[int(map[i][j])], (int(i*scale*9/5), j*scale, WIDTH/size, HEIGHT/size))
            pygame.draw.rect(screen, (255, 255, 255), (int(i*scale*9/5), j*scale, WIDTH/size, HEIGHT/size), 1)

map = create_map(size, level, diff)
print(map)

run = True
while run:
    clock.tick(FPS)
    pygame.draw.rect(screen, (40, 40, 40), (0, 0, WIDTH, HEIGHT+75))
    draw_map()

    if start_button.draw(screen):
        map = create_map(size, level, diff)
        draw_map()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    pygame.display.update()

pygame.quit()