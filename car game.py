import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


car_width, car_height = 50, 100
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 150
car_speed = 7


obstacle_width, obstacle_height = 50, 100
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -100
obstacle_speed = 5


score = 0
font = pygame.font.Font(None, 36)


running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)  # Clear screen

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

   
    obstacle_y += obstacle_speed

   
    if obstacle_y > HEIGHT:
        obstacle_y = -100
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        score += 1
        obstacle_speed += 0.2  # Increase difficulty over time

    
    if (
        car_x < obstacle_x + obstacle_width
        and car_x + car_width > obstacle_x
        and car_y < obstacle_y + obstacle_height
        and car_y + car_height > obstacle_y
    ):
        print("Game Over! Your Score:", score)
        running = False

    
    pygame.draw.rect(screen, BLUE, (car_x, car_y, car_width, car_height))  # Car
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))  # Obstacle

   
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()
