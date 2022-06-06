import pygame

# Initialize pygame
pygame.init()

# Screen properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Continuous")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values
VELOCITY = 5

# Load images
dragon_image = pygame.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Load sounds
sound_2 = pygame.mixer.Sound("sound_2.wav")
sound_2.set_volume(0.2)

# Main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a list of all keys currently being held
    keys = pygame.key.get_pressed()

    # Move the dragon continuosly
    if keys[pygame.K_LEFT]:
        dragon_rect.centerx -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.centerx += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.centery -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.centery += VELOCITY

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()