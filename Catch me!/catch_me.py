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
clown_acceleration = 0.25
score = 0
player_lives = 5

clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set colors
BLUE = (1, 179, 209)
YELLOW = (248, 231, 28)

# Set font
font = pygame.font.Font("Franxurter.ttf", 32)

system_text = font.render("CATCH ME !", True, BLUE, YELLOW)
system_text_rect = system_text.get_rect()
system_text_rect.topleft = (10, 10)

score_text = font.render("SCORE: " + str(score), True, YELLOW, BLUE)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (SCREEN_WIDTH - 20, 10)

lives_text = font.render("LIVES: " + str(player_lives), True, YELLOW, BLUE)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (SCREEN_WIDTH - 20, 50)

gameover_text = font.render("GAME OVER", True, BLUE, YELLOW)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

play_again_text = font.render("CLICK ANYWHERE TO PLAY AGAIN", True, YELLOW, BLUE)
play_again_text_rect = play_again_text.get_rect()
play_again_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 64)

# Game images
# Clown
clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Background
background_image = pygame.image.load("background.png")
background_image_rect = background_image.get_rect()
background_image_rect.topleft = (0, 0)

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
    
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # Check if the clown it's clicked
            if pygame.Rect.collidepoint(clown_rect, mouse_x, mouse_y):
                click_sound.play()
                clown_velocity += clown_acceleration
                score += 1

                # Change clown's direction
                previous_dx = clown_dx
                previous_dy = clown_dy

                # Randomize clown's direction
                while (previous_dx == clown_dx and previous_dy == clown_dy):
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

            # Clown it isn't clicked
            else:
                miss_sound.play()
                clown_velocity += clown_acceleration
                player_lives -= 1
    
    # Move the clown
    clown_rect.x += clown_dx*clown_velocity
    clown_rect.y += clown_dy*clown_velocity

    # Bounce the clown off the edges of the display
    if clown_rect.left <= 0 or clown_rect.right >= SCREEN_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= SCREEN_HEIGHT:
        clown_dy = -1 * clown_dy

    # Update the HUD
    score_text = font.render("SCORE: " + str(score), True, YELLOW, BLUE)
    lives_text = font.render("LIVES: " + str(player_lives), True, YELLOW, BLUE)

    # Check for game over
    if player_lives == 0:
        display_surface.blit(gameover_text, gameover_text_rect)
        display_surface.blit(play_again_text, play_again_text_rect)
        pygame.display.update()

        # Pause the game until the player clicks. Then continue or exit the game
        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():

                # The player wants to play again
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = 5
                    clown_velocity = 3
                    clown_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
                    pygame.mixer.music.play(-1, 0.0)
                    is_paused = False
                
                # The player wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    # Blit the background
    display_surface.blit(background_image, background_image_rect)

    # Blit HUD (Head Up Display)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)
    display_surface.blit(system_text, system_text_rect)

    # Blit the clown
    display_surface.blit(clown_image, clown_rect)

    # Update the screen
    pygame.display.update()
    
    # Tick clock
    clock.tick(FPS)

# End the game
pygame.quit()