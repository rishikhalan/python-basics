import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Subway Surfers")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# Game clock
clock = pygame.time.Clock()

# Player setup
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 120
player_speed = 8

# Obstacle setup
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 7
obstacles = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 28)

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (obs[0], obs[1], obstacle_width, obstacle_height))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    screen.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn new obstacles
    if random.randint(1, 25) == 1:
        x_pos = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([x_pos, -obstacle_height])

    # Move obstacles
    for obs in obstacles:
        obs[1] += obstacle_speed
        if obs[1] > HEIGHT:
            obstacles.remove(obs)
            score += 1

    # Collision detection
    for obs in obstacles:
        if (player_x < obs[0] + obstacle_width and
            player_x + player_size > obs[0] and
            player_y < obs[1] + obstacle_height and
            player_y + player_size > obs[1]):
            game_over()

    # Draw
    draw_player(player_x, player_y)
    draw_obstacles(obstacles)
    show_score(score)

    pygame.display.flip()
    clock.tick(30)
