import pygame
import sys
from player import Player

# Inicialization
pygame.init()
WIDTH, HEIGHT = 640, 480
TILESIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cropy")
clock = pygame.time.Clock()

# Groups
all_sprites = pygame.sprite.Group()
player = Player(pos=(WIDTH//2, HEIGHT//2), tilesize=TILESIZE)
all_sprites.add(player)

# Main Loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((34, 177, 76))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
