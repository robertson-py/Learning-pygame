import pygame
import random

# Initialize pygame module
pygame.init()

# Set basic colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

# Define fonts
font = pygame.font.Font("SuperLegendBoy-4w8Y.ttf", 16)

# Game values
VELOCITY = 10
coin_speed = 2
heart_speed = 2
bonus_speed = 3
bottom_text_limit = 32
score = 0
level = 0
lives = 5

# Define text
score_text = font.render("SCORE: " + str(score), True, GREEN, DARKGREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

title_text = font.render("Feed The Dragon", True, GREEN, DARKGREEN)
title_text_rect = title_text.get_rect()
title_text_rect.centerx = (SCREEN_WIDTH/2)

level_text = font.render("LEVEL: " + str(level), True, GREEN, DARKGREEN)
level_text_rect = level_text.get_rect()
level_text_rect.topright = (780, 10)

lives_text = font.render("LIVES: " + str(lives), True, GREEN, DARKGREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (630, 10)

game_over_text = font.render("GAME OVER", True, GREEN, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

continue_text = font.render("PRESS (Y/N) TO CONTINUE", True, GREEN, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 32)

# Load game images
# Dragon image
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Coin
coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = ((SCREEN_WIDTH + 64), random.randint(bottom_text_limit + 32, SCREEN_HEIGHT - 32))

# Heart (extra live)
heart_image = pygame.image.load("heart.png")
heart_rect = heart_image.get_rect()

# Bonus
bonus_image = pygame.image.load("pinkh.png")
bonus_rect = bonus_image.get_rect()

# Load sounds and music

# Sound effects
# Coin
coin_sound = pygame.mixer.Sound("sound_1.wav")
coin_sound.set_volume(0.25)

# Bonus
bonus_sound = pygame.mixer.Sound("bonus.wav")
bonus_sound.set_volume(0.25)

# Heart
heart_sound = pygame.mixer.Sound("heart.mp3")
heart_sound.set_volume(0.9)

# Missed coin
miss_sound = pygame.mixer.Sound("sound_2.wav")
miss_sound.set_volume(0.3)

# Level up
level_up_sound = pygame.mixer.Sound("sound_3.wav")
level_up_sound.set_volume(0.25)

# Music
music = pygame.mixer.music.load("music_80.wav")
pygame.mixer.music.play(-1, 0.0)

# Set clock and FPS
FPS = 60
clock = pygame.time.Clock()

# Main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make a list of keys
    keys = pygame.key.get_pressed()

    # Smooth movement
    if keys[pygame.K_UP] and dragon_rect.top > bottom_text_limit:
        dragon_rect.centery -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < SCREEN_HEIGHT:
        dragon_rect.centery += VELOCITY
    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.centerx -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < SCREEN_WIDTH:
        dragon_rect.centerx += VELOCITY

    # Cheating setup    
    if keys[pygame.K_KP_MULTIPLY]:
        lives += 1
    if keys[pygame.K_KP_MINUS]:
        coin_speed -= 1
    if keys[pygame.K_KP_PLUS]:
        coin_speed += 1

    # Collision between dragon and coin
    if pygame.Rect.colliderect(dragon_rect, coin_rect):
        coin_sound.play()
        coin_rect.x = (SCREEN_WIDTH + 64 ) # Plus 64 to create the coins out of screen
        coin_rect.y = random.randint(bottom_text_limit + 32, SCREEN_HEIGHT - 32)
        score += 1
        print(coin_speed)

        # Level up condition
        if score % 10 == 0:   
            level += 1
            coin_speed += 1
            level_up_sound.play()

    # Condition to create a heart (extra live)
    if score % 11 == 0 and score > 10:
        heart_rect.x = random.randint(32, SCREEN_WIDTH - 32)
        heart_rect.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 32)
        heart_speed = 2

    # Collision between dragon and heart (extra live)
    if pygame.Rect.colliderect(dragon_rect, heart_rect):
        lives += 1
        heart_sound.play()
        heart_rect.x = 700
        heart_rect.y = 900
        heart_speed = 0

    # Condition to stop uncatched hearts
    if heart_rect.y < bottom_text_limit:
        heart_rect.x = 700
        heart_rect.y = 900
        heart_speed = 0

    # Condition to create a bonus (minus coin speed)
    if score % 25 == 0 and score > 1:
        bonus_rect.x = (SCREEN_WIDTH + 64 ) # Plus 64 to create the coins out of screen
        bonus_rect.y = random.randint(bottom_text_limit + 32, SCREEN_HEIGHT - 32)
        bonus_speed = 3

    # Collision between dragon and bonus
    if pygame.Rect.colliderect(dragon_rect, bonus_rect):
        coin_speed -= 1
        bonus_sound.play()
        bonus_rect.x = 700
        bonus_rect.y = 900
        bonus_speed = 0

    # Condition to stop uncatched bonuses
    if bonus_rect.x < 0:
        bonus_rect.x = 700
        bonus_rect.y = 900
        bonus_speed = 0

    # Condition to lose
    if coin_rect.x < 0:
        coin_rect.x = random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64)
        coin_rect.y = random.randint(bottom_text_limit + 32, SCREEN_HEIGHT - 32)
        lives -= 1
        miss_sound.play()
    
    # Losing condition
    if lives == 0:
        display_surface.blit(game_over_text, game_over_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()

        # Pause the game until player decide to continue playing or not
        pygame.mixer.music.stop()
        is_true = True
        while is_true == True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()

                # Continue playing
                if keys[pygame.K_y]:
                    score = 0
                    lives = 5
                    coin_speed = 2
                    level = 0
                    pygame.mixer.music.play(-1, 0.0)
                    is_true = False
                
                # Exit the game
                elif keys[pygame.K_n]:
                    pygame.quit()

    # Fill the screen
    display_surface.fill((0, 0, 0))

    # Blit the images
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
    display_surface.blit(heart_image, heart_rect)
    display_surface.blit(bonus_image, bonus_rect)

    # Blit the HUD to the screen
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(level_text, level_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    pygame.draw.line(display_surface, GREEN, (0, bottom_text_limit), (SCREEN_WIDTH, bottom_text_limit), 2)

    # Actualize coins and hearts speed
    coin_rect.centerx -= coin_speed
    bonus_rect.centerx -= bonus_speed
    heart_rect.centery -= heart_speed

    # Update the HUD
    lives_text = font.render("LIVES: " + str(lives), True, GREEN, DARKGREEN)
    level_text = font.render("LEVEL: " + str(level), True, GREEN, DARKGREEN)
    score_text = font.render("SCORE: " + str(score), True, GREEN, DARKGREEN)

    # Update the screen
    pygame.display.update()

    # Clock ticking
    clock.tick(FPS)

# End the game
pygame.quit()