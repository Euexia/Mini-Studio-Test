import pygame
import os
import time
import sys
import random
pygame.font.init()


from objects.enemies import *
from objects.spaceship import *
from objects.player import *
from settings import *



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

HIGH_SCORE_FILE = "high_scores.txt"

paused=False

    # ------------------------------------------------------------------
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
    pygame.display.set_caption("Tableau des High Scores")
    screen.fill(WHITE)

    high_scores = read_high_scores()

    while True:


        display_text(screen, "Tableau des High Scores", 40, WIDTH // 2, 50, BLACK)

        for i, score in enumerate(high_scores, start=1):
            display_text(screen, f"{i}. {score}", 30, WIDTH // 2, 100 + i * 40, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
    

   # Load the images of the planets and scale them
    planet1_image = pygame.image.load("assets/planet1.png")
    planet1_image = pygame.transform.scale(planet1_image, (200, 200))
    
    planet2_image = pygame.image.load("assets/planet2.png")
    planet2_image = pygame.transform.scale(planet2_image, (400, 400))
    
    planet3_image = pygame.image.load("assets/planet3.png")
    planet3_image = pygame.transform.scale(planet3_image, (200, 200))
    
    planet4_image = pygame.image.load("assets/planet4.png")
    planet4_image = pygame.transform.scale(planet4_image, (400, 400))
    
    planet5_image = pygame.image.load("assets/planet5.png")
    planet5_image = pygame.transform.scale(planet5_image, (400, 400))


    # Create the rectangles for each planet
    planet1_rect = planet1_image.get_rect(center=(WIDTH/2 - 300, HEIGHT/2 -200))
    planet2_rect = planet2_image.get_rect(center=(WIDTH/2 - 150, HEIGHT/2 +200))
    planet3_rect = planet3_image.get_rect(center=(WIDTH/2, HEIGHT/2 -200))
    planet4_rect = planet4_image.get_rect(center=(WIDTH/2 + 150, HEIGHT/2 + 200))
    planet5_rect = planet5_image.get_rect(center=(WIDTH/2 + 300, HEIGHT/2 -200))


    arrow_image = pygame.image.load("assets/arrow.png")
    arrow_image = pygame.transform.scale(arrow_image, (50, 50))
    arrow_rect = arrow_image.get_rect(bottomleft=(50, HEIGHT-50))


    run = True
    while run:
         # Reset BG to the menu background
        BG = pygame.image.load("assets/background_menu_planet.png").convert_alpha()
        BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
        WIN.blit(BG, (0, 0))
        WIN.blit(planet1_image, planet1_rect)
        WIN.blit(planet2_image, planet2_rect)
        WIN.blit(planet3_image, planet3_rect)
        WIN.blit(planet4_image, planet4_rect)
        WIN.blit(planet5_image, planet5_rect)
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
                    launch_game(1)
                elif planet2_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level2.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    launch_game(2)
                elif planet3_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level3.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    launch_game(3)
                elif planet4_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level4.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    launch_game(4)
                elif planet5_rect.collidepoint(mouse_pos):
                    BG = pygame.image.load("assets/background_level5.png").convert_alpha()
                    BG= pygame.transform.scale(BG, (WIDTH, HEIGHT))
                    launch_game(5)
                elif arrow_rect.collidepoint(mouse_pos):
                    run = False
                    break
BOSS_IMG = pygame.image.load(os.path.join("assets/pixel_ship_red_small.png"))
class Boss(Enemy):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.img = BOSS_IMG
        self.mask = pygame.mask.from_surface(self.img)
        self.health = 100
        self.lasers = []
        self.cool_down_counter = 0

    def move(self, vel):
        self.y += vel

def launch_game(level):
    global run, BG
    run = True
    FPS = 60
    lives = 5

    # Définir les polices de caractères
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

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

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

     # Si toutes les vagues sont terminées, afficher un message de victoire
        if wave == 5:
            winning_bg = pygame.image.load("assets/background_menu.png")
            scaled_bg = pygame.transform.scale(winning_bg, (WIDTH, HEIGHT))
            WIN.blit(scaled_bg, (0, 0))
            win_label = lost_font.render("You Win!!", 1, (255, 255, 255))
            WIN.blit(win_label, (WIDTH / 2 - win_label.get_width() / 2, 350))
            pygame.display.update()
            won = True

        if won and win_time is None:
            win_time = pygame.time.get_ticks()

        if win_time is not None and pygame.time.get_ticks() > win_time + 6000:
            return

        # if wave == 5 and not boss:
        #     boss = Boss(WIDTH/2 - 50, -150, "red")
        #     enemies.append(boss)

        # if boss:
        #     boss.move(boss_vel)
        #     boss.move_lasers(laser_vel, player)
        # if random.randrange(0, 2 * 60) == 1:
        #     boss.shoot()
        # if collide(boss, player):
        #     player.health -= 20
        # if boss.health <= 0:
        #     enemies.remove(boss)
        #     boss = None
        #     wave += 1
        #     wave_length += 5
        #     enemy_vel += 1
        #     for i in range(wave_length):
        #         enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
        #         enemies.append(enemy)

        if len(enemies) == 0:
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