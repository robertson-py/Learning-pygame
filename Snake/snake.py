import pygame, random

# Init pygame
pygame.init()

# Screen properties
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_caption = pygame.display.set_caption("*** SNAKE ***")

# Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
snake_size = 20
head_x = SCREEN_WIDTH/2
head_y = SCREEN_HEIGHT/2
snake_dx = 0
snake_dy = 0
score = 0

# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set font and texts
font = pygame.font.Font("SuperLegendBoy-4w8Y.ttf", 16)

title_text = font.render("SNAKE", True, GREEN, BLACK)
title_text_rect = title_text.get_rect()
title_text_rect.center = (SCREEN_WIDTH/2, 16)

score_text = font.render("SCORE: " + str(score), True, GREEN, BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (SCREEN_WIDTH - 80, 16)

game_over_text = font.render("GAME OVER", True, RED, DARKGREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

continue_text = font.render("DO YOU WANT TO EXIT? (Y/N)", True, RED, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT + 32)

# Line below HUD
line_breaker = pygame.draw.line(display_surface, GREEN, (0, 32), (SCREEN_WIDTH, 32), 1)

# Set values for snake and apple
apple_coordinates = (500, 500, snake_size, snake_size)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coordinates)

head_coordinates = (head_x, head_y, snake_size, snake_size)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coordinates)

body_coordinates = []

# Main game loop
running = True
while running:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the HUD (Head Up Display)
    score_text = font.render("SCORE: " + str(score), True, GREEN, BLACK)

    # Blit the HUD (Head Up Display)
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)

    # Blit assets

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# End the game
pygame.quit()