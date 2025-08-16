import pygame
import sys

# Inicialization
pygame.init()
WIDTH, HEIGHT = 640, 480
TILESIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cropy")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((34, 177, 76))
    pygame.display.flip()

pygame.quit()
sys.exit()
