# def main():
#     global run
#     run = True
#     FPS = 60
#     level = 0
#     lives = 5

#     # définir les polices de caractères
#     main_font = pygame.font.SysFont("comicsans", 50)
#     lost_font = pygame.font.SysFont("comicsans", 60)

#     enemies = []
#     wave_length = 5
#     enemy_vel = 1

#     player_vel = 8
#     laser_vel = 6

#     player = Player(300, 630)

#     clock = pygame.time.Clock()

#     lost = False
#     lost_count = 0





#     def redraw_window():
#         WIN.blit(BG, (0,0))
#         # draw text
#         lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
#         level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

#         WIN.blit(lives_label, (10, 10))
#         WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

#         for enemy in enemies:
#             enemy.draw(WIN)

#         player.draw(WIN)


#         if lost:
#             lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
#             WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

#         pygame.display.update()
        

#     while run:
#         clock.tick(FPS)
#         redraw_window()
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                run = False
#             elif event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_p:
#                 pause_game()

#         if lost:
#             if lost_count > FPS * 3:
#                 run = False
#             else:
#                 continue

#         if len(enemies) == 0:
#             level += 1
#             wave_length += 5
#             for i in range(wave_length):
#                 enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
#                 enemies.append(enemy)


#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_p]:
#            pause_game()
#         if keys[pygame.K_q] and player.x - player_vel > 0: # left
#             player.x -= player_vel
#         if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
#             player.x += player_vel
#         if keys[pygame.K_z] and player.y - player_vel > 0: # up
#             player.y -= player_vel
#         if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
#             player.y += player_vel
#         if keys[pygame.K_SPACE]:
#             player.shoot()

#         for enemy in enemies[:]:
#             enemy.move(enemy_vel)
#             enemy.move_lasers(laser_vel, player)

#             if random.randrange(0, 2*60) == 1:
#                 enemy.shoot()

#             if collide(enemy, player):
#                 player.health -= 10
#                 enemies.remove(enemy)
#             elif enemy.y + enemy.get_height() > HEIGHT:
#                 lives -= 1
#                 enemies.remove(enemy)

#         player.move_lasers(-laser_vel, enemies)


