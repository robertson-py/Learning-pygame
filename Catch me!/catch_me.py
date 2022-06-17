# Import necessary libraries
import pygame

# Initialiaze pygame module
pygame.init()

# Screen properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_caption = pygame.display.set_caption("Catch Me !")

# Game values
clown_velocity = 2
FPS = 60
clock = pygame.time.Clock()

# Game images
clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


# Main game loop
# Logical variable
running = True
position_x = True
position_y = True

# Loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if clown_rect.left == 0:
        position_x = True
    if clown_rect.right == SCREEN_WIDTH:
        position_x = False
    
    if position_x == True:
        clown_rect.x += clown_velocity
    else:
        clown_rect.x -= clown_velocity

    if clown_rect.top == 0:
        position_y = True
    if clown_rect.bottom == SCREEN_HEIGHT:
        position_y = False

    if position_y == True:
        clown_rect.y += clown_velocity
    else:
        clown_rect.y -= clown_velocity
    
    if position_y:
        print(clown_rect.x, clown_rect.y)
    
    display_surface.fill((60, 60, 60))
    display_surface.blit(clown_image, clown_rect)
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()