import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Coders")

# Load assets
car_image = pygame.image.load('car.png')
track_image = pygame.image.load('track.png')
car_image = pygame.transform.scale(car_image, (50, 100))

# Initial car position
car_x, car_y = WIDTH // 2, HEIGHT - 120
car_speed = 5

# Define functions
def draw_track():
    screen.blit(track_image, (0, 0))

def draw_car(x, y):
    screen.blit(car_image, (x, y))

def handle_keys():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        return -car_speed, 0
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        return car_speed, 0
    if keys[pygame.K_UP] and car_y > 0:
        return 0, -car_speed
    if keys[pygame.K_DOWN] and car_y < HEIGHT - 100:
        return 0, car_speed
    return 0, 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle car movement
    dx, dy = handle_keys()
    car_x += dx
    car_y += dy

    # Draw everything
    draw_track()
    draw_car(car_x, car_y)
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Coders")
car_image = pygame.image.load('car.png')
track_image = pygame.image.load('track.png')
car_image = pygame.transform.scale(car_image, (50, 100))
car_x, car_y = WIDTH // 2, HEIGHT - 120
car_speed = 5
def draw_track():
    screen.blit(track_image, (0, 0))

def draw_car(x, y):
    screen.blit(car_image, (x, y))
