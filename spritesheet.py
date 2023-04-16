import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Exemple de sprite sheet")
sprite_sheet = pygame.image.load("stylesheet_planete1.png").convert_alpha()

def get_sprite(sheet, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite
sprite_1 = get_sprite(sprite_sheet, 0, 0, 32, 32)
sprite_2 = get_sprite(sprite_sheet, 32, 0, 32, 32)
# Ajoutez ici les autres sprites à extraire


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(sprite_1, (100, 100))
    screen.blit(sprite_2, (200, 100))
    # Affichez ici les autres sprites

    pygame.display.flip()
