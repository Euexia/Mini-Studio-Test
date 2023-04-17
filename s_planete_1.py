import pygame
import spritesheet
import settings

WIDTH = 1000
HEIGHT = 1000

BG = (50, 50, 50)
BLACK = (0, 0, 0)

def animation_sprite_p(screen):
	sprite_sheet_image_1 = pygame.image.load('stylesheet_planete1.png').convert_alpha()
	sprite_sheet_1 = spritesheet.SpriteSheet(sprite_sheet_image_1)
	
	animation_list_1 = []
	animation_list_2 = []
	animation_list_3 = []
	animation_list_4 = []
	animation_list_5 = []


	animation_steps = 50
	last_update = pygame.time.get_ticks()
	a_cooldown = 100
	frame=0

	for x in range (animation_steps):
		animation_list.append(sprite_sheet.get_image(x, 100, 100, 3, BLACK))

	run = True
	while run:

		#update background

		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= a_cooldown:
			frame +=1
			last_update = current_time
			if frame >= len(animation_list):
				frame = 0

		screen.blit(animation_list[frame],(WIDTH/2 - 300, HEIGHT/2 -200))

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		pygame.display.update()

	pygame.quit()