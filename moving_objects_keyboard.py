import pygame

# Initialize pygame modul
pygame.init()

# Create a surface object
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption

# Set game values
VELOCITY = 30

# Load in images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = SCREEN_WIDTH/2
dragon_rect.bottom = SCREEN_HEIGHT

# Main loop
running = True
while running == True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        # Check for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.centerx -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.centerx += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.centery -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.centery += VELOCITY
    # Fill the display surface to cover old images
    display_surface.fill((0, 0, 0))
    # Blit (copy) assets to the screen
    display_surface.blit(dragon_image, dragon_rect)

    # Update the screen
    pygame.display.update()

# End the game
pygame.quit()