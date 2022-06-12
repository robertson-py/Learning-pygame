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

# Define text
score_text = font.render("Feed The Dragon", True, GREEN, DARKGREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

# Load game images
# Dragon image
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# Coin
coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64), random.randint(0, SCREEN_HEIGHT - 32))

# Load sounds and music
coin_sound = pygame.mixer.Sound("sound_1.wav")
coin_sound.set_volume(0.3)

# Game values
VELOCITY = 10
coin_speed = 2
coins_lost = 0
collisions = 0
score = 0
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

    if keys[pygame.K_UP] and dragon_rect.top > 0:
        dragon_rect.centery -= VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < SCREEN_HEIGHT:
        dragon_rect.centery += VELOCITY
    if keys[pygame.K_LEFT] and dragon_rect.left > 0:
        dragon_rect.centerx -= VELOCITY
    if keys[pygame.K_RIGHT] and dragon_rect.right < SCREEN_WIDTH:
        dragon_rect.centerx += VELOCITY

    # Fill the screen
    display_surface.fill((0, 0, 0))

    # Blit the images
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
    display_surface.blit(score_text, score_text_rect)
    coin_rect.centerx -= coin_speed

    # Collisions
    if pygame.Rect.colliderect(dragon_rect, coin_rect):
        coin_sound.play()
        coin_rect.x = random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64)
        coin_rect.y = random.randint(0, SCREEN_HEIGHT - 32)
        score += 1
        collisions += 1
        if collisions%5 == 0:
            coin_speed += 1

    if coin_rect.x < 0:
        coin_rect.x = random.randint(SCREEN_WIDTH + 64, SCREEN_WIDTH + 64)
        coin_rect.y = random.randint(0, SCREEN_HEIGHT - 32)
        coins_lost += 1
        if coins_lost == 5:
            running = False

    # Update the screen
    pygame.display.update()

    # Clock ticking
    clock.tick(FPS)

# End the game
pygame.quit()