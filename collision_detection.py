import pygame
import random

# Initialize pygame module
pygame.init()

# Settings
VELOCITY = 5

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Screen properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")

# Load images
# Dragon
dragon_image = pygame.image.load("male.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Coin
coin_image = pygame.image.load("pill.png")
coin_rect = coin_image.get_rect()
coin_rect.topright = (750, 550)

# Load sounds
coin_sound = pygame.mixer.Sound("coin.wav")

# Main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Moving the dragon
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and dragon_rect.left > 0:
        dragon_rect.centerx -= VELOCITY
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and dragon_rect.right < SCREEN_WIDTH:
        dragon_rect.centerx += VELOCITY
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and dragon_rect.top > 0:
        dragon_rect.centery -= VELOCITY
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and dragon_rect.bottom < SCREEN_HEIGHT:
        dragon_rect.centery += VELOCITY

    # Check for collisions between two rect objects
    if dragon_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.x = random.randint(0, SCREEN_WIDTH - 32)
        coin_rect.y = random.randint(0, SCREEN_HEIGHT - 32)
        coin_sound.play()
        # pygame.time.delay(1000)

    # Fill the screen
    display_surface.fill((50, 50, 50))
    
    # Draw a rectangle arround our rects
    # pygame.draw.rect(display_surface, (0, 255, 0), dragon_rect, 1)
    # pygame.draw.rect(display_surface, (255, 255, 0), coin_rect, 1)

    # Blit the assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)

    # Update display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()