# Import necessary libraries
import pygame
import random

# Initialiaze pygame module
pygame.init()

# Screen properties
SCREEN_WIDTH = 945
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_caption = pygame.display.set_caption("Catch Me !")

# Set game values
clown_velocity = 3
clown_acceleration = 0.5
score = 0
player_lives = 0

clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set colors
BLUE = (1, 179, 209)
YELLOW = (248, 231, 28)

# Set font
main_font = pygame.font.Font("SuperLegendBoy-4w8Y.ttf", 16)

system_text = pygame.font.Font.render("Catch Me !", True, BLUE, YELLOW)
system_text_rect = system_text.get_rect()
system_text_rect.topleft = (10, 10)

score_text = pygame.font.Font.render("Score: " + str(score), True, YELLOW, BLUE)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (800, 10)

lives_text = pygame.font.Font.render("LIVES: " + str(player_lives), True, YELLOW, BLUE)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (800, 32)

gameover_text = pygame.font.Font.render("GAME OVER", True, BLUE, YELLOW)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

play_again_text = pygame.font.Font.render("CLICK ANYWHERE TO PLAY AGAIN", True, YELLOW, BLUE)
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 32)

# Game images
# Clown
clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Background


# Set sound and music
# Sounds
click_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")

# Music
background_music = pygame.mixer.music.load("bgr_music.wav")
pygame.mixer.music.play(-1, 0.0)

# Logical variables
running = True
position_x = True
position_y = True

# Main game loop
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Conditions to make the clown move left or right
    if clown_rect.left == 0:
        position_x = True
    if clown_rect.right == SCREEN_WIDTH:
        position_x = False
    
    # Clown X axis movement
    if position_x == True:
        clown_rect.x += clown_velocity  # Move right
    else:
        clown_rect.x -= clown_velocity  # Move left

    # Conditions to make the clown move up or down
    if clown_rect.top == 0:
        position_y = True
    if clown_rect.bottom == SCREEN_HEIGHT:
        position_y = False

    # Clown Y axis movement
    if position_y == True:
        clown_rect.y += clown_velocity  # Move down
    else:
        clown_rect.y -= clown_velocity  # Move up
    
    if position_y:
        print(clown_rect.x, clown_rect.y)
    
    display_surface.fill((60, 60, 60))
    display_surface.blit(clown_image, clown_rect)
    pygame.display.update()
    clock.tick(FPS)

# End the game
pygame.quit()