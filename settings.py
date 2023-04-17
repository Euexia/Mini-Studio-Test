import pygame
import os
import time
import random

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyberspace Chaos")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_menu.png")), (WIDTH, HEIGHT))

main_font = pygame.font.Font("researcher-researcher-bold-700.ttf", 50)


def display_text(screen, text, size, x, y, color):
    font = pygame.font.Font("researcher-researcher-bold-700.ttf", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)