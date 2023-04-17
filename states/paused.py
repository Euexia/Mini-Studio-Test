import pygame
import os
import time
import sys
import random

from settings import *

paused = False



def pause_game():
    pygame.time.delay(200)
    global paused, run
    paused = not paused
    run = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                paused = False
                break
        # Draw pause menu
        pause_label = pygame.font.Font(None, 100).render("Pause", True, (255, 255, 255))
        pause_rect = pause_label.get_rect(centerx=WIDTH/2, top=HEIGHT/2 - 200)
        continue_label = main_font.render("Continuer", 1, (255, 255, 255))
        continue_rect = continue_label.get_rect(centerx=WIDTH/2, centery=HEIGHT/2 - 10)
        quit_label = main_font.render("Quitter la partie", 1, (255, 255, 255))
        quit_rect = quit_label.get_rect(centerx=WIDTH/2, centery=HEIGHT/2 + 100)


        WIN.blit(pause_label, pause_rect)
        WIN.blit(continue_label, continue_rect)
        WIN.blit(quit_label, quit_rect)

        # Check for button clicks
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if continue_rect.collidepoint(mouse_pos):
                paused = False
            elif quit_rect.collidepoint(mouse_pos):
                run = False
                paused = False

        pygame.display.update()