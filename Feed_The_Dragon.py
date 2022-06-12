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
###coins_lost = 0
collisions = 0
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
level_text_rect.topright = (790, 10)

lives_text = font.render("LIVES: " + str(lives), True, GREEN, DARKGREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (650, 10)

# Load game images
# Dragon image
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# Coin
coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64), random.randint(bottom_text_limit, SCREEN_HEIGHT - 32))
# Heart (extra live)
heart_image = pygame.image.load("heart.png")
heart_rect = heart_image.get_rect()
heart_rect.bottomleft = (random.randint(32, SCREEN_WIDTH - 32), random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 32))

# Load sounds and music
coin_sound = pygame.mixer.Sound("sound_1.wav")
coin_sound.set_volume(0.3)
miss_sound = pygame.mixer.Sound("sound_2.wav")
miss_sound.set_volume(0.5)
level_up_sound = pygame.mixer.Sound("sound_3.wav")
level_up_sound.set_volume(0.4)

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

    # Collision between dragon and coin
    if pygame.Rect.colliderect(dragon_rect, coin_rect):
        coin_sound.play()
        coin_rect.x = random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64) # Plus 64 to create the coins out of screen
        coin_rect.y = random.randint(bottom_text_limit, SCREEN_HEIGHT - 32)
        score += 1
        collisions += 1
        score_text = font.render("SCORE: " + str(score), True, GREEN, DARKGREEN)

        # Condition to increase coin's speed
        if collisions%5 == 0:
            coin_speed += 1
            level += 1
            level_text = font.render("LEVEL: " + str(level), True, GREEN, DARKGREEN)
            level_up_sound.play()

    # # Collision between dragon and heart (extra live)
    # if pygame.Rect.colliderect(dragon_rect, heart_rect):
    #     heart_rect.x = random.randint(32, SCREEN_WIDTH - 32)
    #     heart_rect.y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT + 32)
    #     lives += 1
    #     level_up_sound.play()
    #     lives_text = font.render("LIVES: " + str(lives), True, GREEN, DARKGREEN)

    # Condition to lose
    if coin_rect.x < 0:
        coin_rect.x = random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64)
        coin_rect.y = random.randint(16, SCREEN_HEIGHT - 32)
        ###coins_lost += 1
        lives -= 1
        miss_sound.play()
        lives_text = font.render("LIVES: " + str(lives), True, GREEN, DARKGREEN)

        # Losing condition
        if lives == 0:
            running = False
    
    # Fill the screen
    display_surface.fill((0, 0, 0))

    # Blit the images
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
    #display_surface.blit(heart_image, heart_rect)

    # Blit the text
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(level_text, level_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    coin_rect.centerx -= coin_speed
    heart_rect.centery -= coin_speed

    # Update the screen
    pygame.display.update()

    # Clock ticking
    clock.tick(FPS)

# End the game
pygame.quit()