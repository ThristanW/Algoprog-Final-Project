import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Map dimensions and layout
MAP_WIDTH, MAP_HEIGHT = 10, 10
TILE_SIZE = 64  # Size of each tile in pixels

# Simple maze layout (1 = wall, 0 = empty space)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Player settings
player_x = 150
player_y = 150
player_angle = 0
FOV = math.pi / 3  # 60 degrees
RAY_COUNT = 120
MAX_DEPTH = 800
PLAYER_SPEED = 3
ROTATION_SPEED = 0.05

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raycasting with Player")
clock = pygame.time.Clock()

# Load textures
floor_texture = pygame.image.load("Algoprog/Final Project/resources/textures/floor1.png")
ceiling_texture = pygame.image.load("Algoprog/Final Project/resources/textures/ceiling1.png")

# Scale textures to tile size
floor_texture = pygame.transform.scale(floor_texture, (TILE_SIZE, TILE_SIZE))
ceiling_texture = pygame.transform.scale(ceiling_texture, (TILE_SIZE, TILE_SIZE))

# Helper functions
def draw_ceiling_and_floor():
    """Draw the physical ceiling and floor with textures."""
    for y in range(HALF_HEIGHT + 1, HEIGHT):
        # Distance from the player's view to the floor line
        row_distance = HEIGHT / (2.0 * y - HEIGHT + 0.001)  # Add a small offset to prevent zero division

        for x in range(WIDTH):
            # Calculate the floor projection point
            camera_x = 2 * x / WIDTH - 1
            floor_x = player_x + row_distance * (math.cos(player_angle) + camera_x * math.sin(player_angle))
            floor_y = player_y + row_distance * (math.sin(player_angle) - camera_x * math.cos(player_angle))

            # Tile positions
            tile_x = int(floor_x) % TILE_SIZE
            tile_y = int(floor_y) % TILE_SIZE

            # Blit floor texture
            screen.blit(floor_texture, (x, y), (tile_x, tile_y, 1, 1))

            # Blit ceiling texture
            screen.blit(ceiling_texture, (x, HEIGHT - y), (tile_x, tile_y, 1, 1))

def raycasting():
    """Perform raycasting and render the walls."""
    for ray in range(RAY_COUNT):
        # Calculate ray angle
        ray_angle = player_angle - FOV / 2 + (ray / RAY_COUNT) * FOV

        # Step sizes for DDA
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        # Distance to wall
        for depth in range(MAX_DEPTH):
            target_x = player_x + depth * cos_a
            target_y = player_y + depth * sin_a

            # Map coordinates
            map_x = int(target_x // TILE_SIZE)
            map_y = int(target_y // TILE_SIZE)

            # Ensure map bounds
            if map_x < 0 or map_x >= MAP_WIDTH or map_y < 0 or map_y >= MAP_HEIGHT:
                break

            # Break if we hit a wall
            if MAP[map_y][map_x] == 1:
                # Calculate perpendicular distance (to remove fisheye effect)
                depth *= math.cos(player_angle - ray_angle)

                # Calculate wall height
                wall_height = min(HEIGHT, TILE_SIZE * HEIGHT / (depth + 0.1))

                # Wall color
                color = WHITE if map_x % 2 == 0 else BLUE

                # Draw wall slice
                pygame.draw.rect(
                    screen,
                    color,
                    (ray * (WIDTH // RAY_COUNT), HALF_HEIGHT - wall_height // 2, WIDTH // RAY_COUNT, wall_height),
                )
                break

def draw_player():
    """Draw the player as a small circle on the map."""
    pygame.draw.circle(screen, RED, (int(player_x), int(player_y)), 5)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move forward
        player_x += PLAYER_SPEED * math.cos(player_angle)
        player_y += PLAYER_SPEED * math.sin(player_angle)
    if keys[pygame.K_s]:  # Move backward
        player_x -= PLAYER_SPEED * math.cos(player_angle)
        player_y -= PLAYER_SPEED * math.sin(player_angle)
    if keys[pygame.K_a]:  # Rotate left
        player_angle -= ROTATION_SPEED
    if keys[pygame.K_d]:  # Rotate right
        player_angle += ROTATION_SPEED

    # Draw the ceiling, floor, walls, and player
    screen.fill(BLACK)
    draw_ceiling_and_floor()
    raycasting()
    draw_player()

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
