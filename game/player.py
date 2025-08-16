import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tilesize):
        super().__init__()
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self.input()
