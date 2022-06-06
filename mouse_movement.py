import pygame

# Initialize pygame module
pygame.init()

# Screen surface
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse movement")

# Time setup
clock = pygame.time.Clock()

# Load images
dragon_image = pygame.image.load("dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25, 25)

# Load sounds
sound_1 = pygame.mixer.Sound("sound_2.wav")
sound_1.set_volume(0.5)

# Main game loop
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # Move based on mouse clicks and motion
        if event.type == pygame.MOUSEMOTION:
        #if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_rect.centerx = mouse_x
            dragon_rect.centery = mouse_y
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound_1.play()

    # Fill the display
    display_surface.fill((0, 0, 0))

    # Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    
    # Update the screen
    pygame.display.update()
    pygame.mouse.set_visible(False)

    clock.tick(60)

# End the game
pygame.quit()