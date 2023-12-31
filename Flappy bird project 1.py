import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Colors
background_color = (255, 255, 255)
bird_color = (255, 0, 0)
pipe_color = (0, 128, 0)

# Bird properties
bird_x = 100
bird_y = 250
bird_y_speed = 0
bird_radius = 30

# Pipe properties
pipe_width = 50
pipe_gap = 500
pipe_x = WIDTH
pipe_heights = [random.randint(100, HEIGHT - 100) for _ in range(3)]
pipe_speed = 5

# Game variables
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_speed = -10

    bird_y_speed += 1
    bird_y += bird_y_speed

    # Update pipes
    pipe_x -= pipe_speed
    if pipe_x < -pipe_width:
        pipe_x = WIDTH
        pipe_heights = [random.randint(100, HEIGHT - 100) for _ in range(3)]

    # Check collision with pipes
    for pipe_height in pipe_heights:
        if pipe_x < bird_x + bird_radius < pipe_x + pipe_width and (bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap):
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(background_color)
    pygame.draw.circle(screen, bird_color, (bird_x, bird_y), bird_radius)

    for pipe_height in pipe_heights:
        pygame.draw.rect(screen, pipe_color, (pipe_x, 0, pipe_width, pipe_height))
        pygame.draw.rect(screen, pipe_color, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

    score_text = font.render(f"Score: {score}", True, (10, 10,10))
    screen.blit(score_text, (1, 1))

    pygame.display.update()
    clock.tick(30)
