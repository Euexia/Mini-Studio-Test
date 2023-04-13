import pygame
import os
import time
import random
pygame.font.init()

from objects.enemies import *
from objects.spaceship import *
from objects.player import *
from settings import *




def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)


def main_menu():
    title_font = pygame.font.SysFont("Serif Bold", 90)
    button_font = pygame.font.SysFont("Serif Bold", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("CyberSpace Chaos", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 200))

        # Ajoutez un bouton pour jouer le jeu
        play_button = pygame.Rect(0, 0, 200, 50)
        play_button.center = (WIDTH/2, 500)
        play_button_surf = pygame.Surface(play_button.size, pygame.SRCALPHA)
        pygame.draw.rect(play_button_surf, (255, 0, 0, 0), play_button_surf.get_rect())
        WIN.blit(play_button_surf, play_button)
        play_label = button_font.render("Play", 1, (255, 255, 255))
        WIN.blit(play_label, (play_button.centerx - play_label.get_width()/2, play_button.centery - play_label.get_height()/2))

        # Ajoutez un bouton pour quitter le programme
        quit_button = pygame.Rect(0, 0, 200, 50)
        quit_button.center = (WIDTH/2, 600)
        quit_button_surf = pygame.Surface(quit_button.size, pygame.SRCALPHA)
        pygame.draw.rect(quit_button_surf, (255, 0, 0, 0), quit_button_surf.get_rect())
        WIN.blit(quit_button_surf, quit_button)
        quit_label = button_font.render("Quit", 1, (255, 255, 255))
        WIN.blit(quit_label, (quit_button.centerx - quit_label.get_width()/2, quit_button.centery - quit_label.get_height()/2))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Si le joueur clique sur le bouton pour jouer, lancez le jeu
                if play_button.collidepoint(mouse_pos):
                    main()
                # Si le joueur clique sur le bouton pour quitter, quittez le programme
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

main_menu()