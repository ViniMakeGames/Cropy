import pygame, os
ASSETS_DIR = "game\\assets\sprites"

def load_img(name, size):
    path = os.path.join(ASSETS_DIR, f"{name}.png")
    img = pygame.image.load(path).convert_alpha()
    if img.get_size() != size:
        img = pygame.transform.scale(img, size)
    return img