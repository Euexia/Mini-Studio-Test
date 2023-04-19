import pygame
import os
import time
import sys
import random
import spritesheet

pygame.font.init()

from s_planete_1 import animation_sprite_p
from objects.enemies import *
from objects.spaceship import *
from objects.player import *
from settings import *


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HIGH_SCORE_FILE = "high_scores.txt"

paused=False

    # ------------------------------------------------------------------

def display_text(screen, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def read_high_scores():
    if not os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write("0\n0\n0\n0\n0")

    with open(HIGH_SCORE_FILE, "r") as f:
        scores = [int(line.strip()) for line in f.readlines()]

    return scores

def write_high_scores(scores):
    with open(HIGH_SCORE_FILE, "w") as f:
        for score in scores:
            f.write(str(score) + "\n")

def update_high_scores(new_score):
    scores = read_high_scores()
    scores.append(new_score)
    scores.sort(reverse=True)
    scores = scores[:5]  # Gardez les 5 meilleurs scores
    write_high_scores(scores)
    return scores


def show_high_scores():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    main_font = pygame.font.Font("INVASION2000.TTF", 50)

    pygame.display.set_caption(main_font.render(f"Tableau des High scores", 1, (255, 255, 255)))
    BG = pygame.image.load("assets/background_menu_planet.png").convert_alpha()
    BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
    WIN.blit(BG, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    arrow_image = pygame.image.load("assets/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (50, 50))
    arrow_rect = arrow_image.get_rect(bottomleft=(50, HEIGHT-50))

    high_scores = read_high_scores()

    while True:
        if arrow_rect.collidepoint(mouse_pos):
            main_menu()

        display_text(screen, "Tableau des High Scores", 40, WIDTH // 2, 50, WHITE)

        for i, score in enumerate(high_scores, start=1):
            display_text(screen, f"{i}. {score}", 30, WIDTH // 2, 100 + i * 40, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if arrow_rect.collidepoint(mouse_pos):
                    main_menu()

        pygame.display.flip()

def enter_name():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Entrez votre nom")

    input_name = ""
    input_done = False

    while not input_done:
        screen.fill(WHITE)

        display_text(screen, "Entrez votre nom :", 30, WIDTH // 2, HEIGHT // 2 - 50, BLACK)
        display_text(screen, input_name, 30, WIDTH // 2, HEIGHT // 2, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_done = True
                elif event.key == pygame.K_BACKSPACE:
                    input_name = input_name[:-1]
                else:
                    input_name += event.unicode

        pygame.display.flip()

    return input_name

    # ------------------------------------------------------------------

def pause_game():
    pygame.time.delay(200)
    global paused, run
    paused = not paused
    run = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                paused = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()
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
    
    # ------------------------------------------------------------------
BG = pygame.image.load("assets/background_menu.png").convert_alpha()
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

def planet_menu():
    global BG
    
    sprite_sheet_image_1 = pygame.image.load('stylesheet_planete1.png').convert_alpha()
    sprite_sheet_1 = spritesheet.SpriteSheet(sprite_sheet_image_1)
    sprite_sheet_image_2 = pygame.image.load('stylesheet_planete2.png').convert_alpha()
    sprite_sheet_2 = spritesheet.SpriteSheet(sprite_sheet_image_2)
    sprite_sheet_image_3 = pygame.image.load('stylesheet_blackhole1.png').convert_alpha()
    sprite_sheet_3 = spritesheet.SpriteSheet(sprite_sheet_image_3)
    sprite_sheet_image_4 = pygame.image.load('stylesheet_planete_4.png').convert_alpha()
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
        planet1_image = sprite_sheet_1.get_image(x, 100, 100, 2, BLACK)
        animation_list_1.append(planet1_image)

        planet2_image = sprite_sheet_2.get_image(x, 100, 100, 2, BLACK)
        animation_list_2.append(planet2_image)

        planet3_image = sprite_sheet_3.get_image(x, 200, 150, 2, BLACK)
        animation_list_3.append(planet3_image)

        planet4_image = sprite_sheet_4.get_image(x, 200, 150, 2, BLACK)
        animation_list_4.append(planet4_image)

        planet5_image = sprite_sheet_5.get_image(x, 300, 300, 2, BLACK)
        animation_list_5.append(sprite_sheet_5.get_image(x, 300, 300, 2, BLACK))


   # Load the images of the planets and scale them
    #planet1_image = pygame.image.load("assets/planet1.png")
    #planet1_image = pygame.transform.scale(planet1_image, (200, 200))
    
    #planet2_image = pygame.image.load("assets/planet2.png")
    #planet2_image = pygame.transform.scale(planet2_image, (400, 400))
    #
    #planet3_image = pygame.image.load("assets/planet3.png")
    #planet3_image = pygame.transform.scale(planet3_image, (200, 200))
    #
    #planet4_image = pygame.image.load("assets/planet4.png")
    #planet4_image = pygame.transform.scale(planet4_image, (400, 400))
    #
    #planet5_image = pygame.image.load("assets/planet5.png")
    #planet5_image = pygame.transform.scale(planet5_image, (400, 400))


    # Create the rectangles for each planet
    planet1_rect = planet1_image.get_rect(center=(WIDTH/2 - 300, HEIGHT/2 -200))
    planet2_rect = planet2_image.get_rect(center=(WIDTH/2 - 150, HEIGHT/2 +200))
    planet3_rect = planet3_image.get_rect(center=(WIDTH/2, HEIGHT/2 -200))
    planet4_rect = planet4_image.get_rect(center=(WIDTH/2 + 150, HEIGHT/2 + 200))
    planet5_rect = planet5_image.get_rect(center=(WIDTH/2 + 300, HEIGHT/2 -200))


    arrow_image = pygame.image.load("assets/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (50, 50))
    arrow_rect = arrow_image.get_rect(bottomleft=(50, HEIGHT-50))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= a_cooldown or last_update == 0:
            frame +=1
            
            last_update = current_time
            if frame >= 50:
                frame = 0
        # Reset BG to the menu background
        BG = pygame.image.load("assets/background_menu_planet.png").convert_alpha()
        BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
        WIN.blit(BG, (0, 0))
        WIN.blit(animation_list_1[frame],planet1_rect)
        WIN.blit(animation_list_2[frame],planet2_rect)
        WIN.blit(animation_list_3[frame],planet3_rect)
        WIN.blit(animation_list_4[frame],planet4_rect)
        WIN.blit(animation_list_5[frame],planet5_rect)
        WIN.blit(arrow_image, arrow_rect)
        pygame.display.update()

    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if planet1_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level1.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    main(1)
                elif planet2_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level2.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    main(2)
                elif planet3_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level3.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    main(3)
                elif planet4_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level4.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    main(4)
                elif planet5_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level5.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    main(5)
                elif arrow_rect.collidepoint(mouse_pos):
                    run = False
                    main_menu()

    def move(self, vel):
        self.y += vel

BOSS_IMG = pygame.image.load(os.path.join("assets/boss.png"))
class Boss:
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y + 350
        self.health = 500
        self.vel = 2
        self.direction = "droite"
        self.img = pygame.image.load(img_path)
        self.mask = pygame.mask.from_surface(self.img)
        self.lasers = []
        self.laser_img = pygame.image.load("assets/pixel_laser_red.png")
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, vel):
        if self.direction == "droite":
            self.x += vel
            if self.x + self.img.get_width() > pygame.display.Info().current_w:
                self.direction = "gauche"
        else:
            self.x -= vel
            if self.x < 0:
                self.direction = "droite"

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def shoot_2(self):
        if self.cool_down_counter == 0:
            laser1 = Laser(self.x - 40, self.y, self.laser_img)
            laser2 = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser1)
            self.lasers.append(laser2)
            self.cool_down_counter = 1

    def move_lasers(self, vel, obj):
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
            elif len(self.lasers) == 2 and laser == self.lasers[0] and self.lasers[1].off_screen(HEIGHT):
                self.lasers.remove(laser)
                break


def start_boss(level):
    global run, BG
    run = True
    FPS = 60
    lives = 5

    # Définir les polices de caractères
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    player_vel = 8
    laser_vel = 10

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # Définir les variables du boss
    boss = Boss(WIDTH / 2 - 50, -300, "assets/boss.png")
    boss_vel = 2
    boss_laser_vel = 8

    while run:
        clock.tick(FPS)

        # Gérer les événements
        
    # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    planet_menu()


        # Déplacer le boss
        boss.move(boss_vel)

        # Dessiner les éléments du jeu
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause_game()
    
        if keys[pygame.K_q] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_z] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
    
        if keys[pygame.K_SPACE]:
            player.shoot()
    
    
        # Vérifier si le joueur est touché par un laser du boss
        if collide(player, boss):
            player.health -= 10

        # Vérifier si le boss a été touché par un laser du joueur
        for laser in player.lasers:
            if collide(laser, boss):
                player.lasers.remove(laser)
                boss.health -= 10

        # Si le boss a perdu tous ses points de vie, arrêter la boucle de jeu et revenir au menu principal
        if boss.health <= 0:
            planet_menu()

        # Si le joueur n'a plus de points de vie, afficher un message de défaite
        if player.health <= 0:
            lost = True
            lost_count += 1

        # Si le joueur a perdu trois fois, arrêter la boucle de jeu et revenir au menu principal
        if lost:
            if lost_count > FPS * 3:
                planet_menu()
            else:
                lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
                WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
        else:
            player.move_lasers(-laser_vel, [])
            player.draw(WIN)

        boss.move_lasers(boss_laser_vel, player)
        boss.draw(WIN)

        pygame.display.update()


def main(level):
    global run, BG, SCORE
    run = True
    global FPS
    FPS =60
    lives = 5

    # Définir les polices de caractères
    main_font = pygame.font.Font("INVASION2000.TTF", 50)
    lost_font = pygame.font.Font("INVASION2000.TTF", 60)

    player_vel = 8
    laser_vel = 6

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # Définir les variables de vagues
    enemies = []
    wave_length = 5
    enemy_vel = 1
    wave = 0
    max_waves = 5
    won = False
    win_time = None
    boss = None
    boss_vel = 3

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Afficher le texte
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        wave_label = main_font.render(f"Wave: {wave}/{max_waves}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(wave_label, (WIDTH / 2 - wave_label.get_width() / 2, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)



        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
            #pygame.time.wait(3000)
            name = enter_name()
            update_high_scores(int(SCORE))
            main_menu()

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1


# Si toutes les vagues sont terminées, afficher un message de victoire
        if won and win_time is None:
            win_time = pygame.time.get_ticks()
    
        if win_time is not None and pygame.time.get_ticks() > win_time + 6000:
            return
    
        if len(enemies) == 0 and wave < max_waves:
            wave += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause_game()
    
        if keys[pygame.K_q] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_z] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
    
        if keys[pygame.K_SPACE]:
            player.shoot()
    
        


        if wave == max_waves:
            start_boss(1)
            boss_present = True
            if random.randrange(0, 2 * 30) == 1:
                Boss.shoot_1()
                Boss.shoot_2()
    
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
    
            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()
    
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
    
        player.move_lasers(-laser_vel, enemies)


# -----------------------------------------------------------------------------------------------------
def main_menu():
    # définir les polices de caractères
    title_font = pygame.font.SysFont("Serif Bold", 90)
    button_font = pygame.font.SysFont("Serif Bold", 70)


    run = True


    while run:
        BG = pygame.image.load("assets/background_menu.png").convert_alpha()
        BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
        WIN.blit(BG, (0,0))
        title_label = title_font.render("CyberSpace Chaos", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 200))

        # Ajoutez un bouton pour sélectionner une planète
        planet_button = pygame.Rect(0, 0, 200, 50)
        planet_button.center = (WIDTH/2, 400)
        planet_button_surf = pygame.Surface(planet_button.size, pygame.SRCALPHA)
        pygame.draw.rect(planet_button_surf, (255, 0, 0, 0), planet_button_surf.get_rect())
        WIN.blit(planet_button_surf, planet_button)
        planet_label = button_font.render("Select a planet", 1, (255, 255, 255))
        WIN.blit(planet_label, (planet_button.centerx - planet_label.get_width()/2, planet_button.centery - planet_label.get_height()/2))

        score_button = pygame.Rect(0, 0, 200, 50)
        score_button.center = (WIDTH/2, 500)
        score_button_surf = pygame.Surface(score_button.size, pygame.SRCALPHA)
        pygame.draw.rect(score_button_surf, (255, 0, 0, 0), score_button_surf.get_rect())
        WIN.blit(score_button_surf, planet_button)
        score_label = button_font.render("Highscore", 1, (255, 255, 255))
        WIN.blit(score_label, (score_button.centerx - score_label.get_width()/2, score_button.centery - score_label.get_height()/2))

        # Ajoutez un bouton pour quitter le programme
        quit_button = pygame.Rect(0, 0, 200, 50)
        quit_button.center = (WIDTH/2, 600)
        quit_button_surf = pygame.Surface(quit_button.size, pygame.SRCALPHA)
        pygame.draw.rect(quit_button_surf, (255, 0, 0, 0), quit_button_surf.get_rect())
        WIN.blit(quit_button_surf, quit_button)
        quit_label = button_font.render("Quit", 1, (255, 255, 255))
        WIN.blit(quit_label, (quit_button.centerx - quit_label.get_width()/2, quit_button.centery - quit_label.get_height()/2))
        mouse_pos = pygame.mouse.get_pos()
        if planet_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                planet_menu() # Appel de la fonction select_planet_menu() pour sélectionner une planète

        
        pygame.display.update()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Si le joueur clique sur le bouton pour jouer, lancez le jeu
                if planet_button.collidepoint(mouse_pos):
                    planet_menu()
                elif score_button.collidepoint(mouse_pos):
                    show_high_scores()
                # Si le joueur clique sur le bouton pour quitter, quittez le programme
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()

main_menu()