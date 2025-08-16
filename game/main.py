import pygame
import sys
from player import Player
from map import draw_map, get_collision_tiles

# Inicialization
pygame.init()
WIDTH, HEIGHT = 640, 480
TILESIZE = 32
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cropy")
clock = pygame.time.Clock()

collision_tiles = get_collision_tiles(TILESIZE)

# Groups
all_sprites = pygame.sprite.Group()
player = Player(pos=(WIDTH//2, HEIGHT//2), tilesize=TILESIZE, walls=collision_tiles)
all_sprites.add(player)

# Main Loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    draw_map(screen, TILESIZE)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
