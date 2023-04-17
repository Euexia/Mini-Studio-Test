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
	
	sprite_sheet_image_2 = pygame.image.load('stylesheet_planete2.png').convert_alpha()
	sprite_sheet_2 = spritesheet.SpriteSheet(sprite_sheet_image_2)
	sprite_sheet_image_3 = pygame.image.load('stylesheet_blackhole1.png').convert_alpha()
	sprite_sheet_3 = spritesheet.SpriteSheet(sprite_sheet_image_3)
	sprite_sheet_image_4 = pygame.image.load('stylesheet_planete1.png').convert_alpha()
	sprite_sheet_4 = spritesheet.SpriteSheet(sprite_sheet_image_4)
	sprite_sheet_image_5 = pygame.image.load('stylesheet_planete5.png').convert_alpha()
	sprite_sheet_5 = spritesheet.SpriteSheet(sprite_sheet_image_5)

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
		animation_list_1.append(sprite_sheet_1.get_image(x, 100, 100, 3, BLACK))
		animation_list_2.append(sprite_sheet_2.get_image(x, 100, 100, 3, BLACK))
		animation_list_3.append(sprite_sheet_3.get_image(x, 200, 150, 3, BLACK))
		animation_list_4.append(sprite_sheet_4.get_image(x, 200, 150, 3, BLACK))

	run = True
	while run:

		#update animation
		current_time = pygame.time.get_ticks()
		if current_time - last_update >= a_cooldown:
			frame +=1
			last_update = current_time
			if frame >= 50:
				frame = 0

		screen.blit(animation_list_1[frame],(WIDTH/2 - 300, HEIGHT/2 -200))


