import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tilesize, walls):
        super().__init__()
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.speed = 2
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.walls = walls
        self.facing = pygame.math.Vector2(0, 1)

    def input(self):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed

        if dx or dy:
            fx = (dx > 0) - (dx < 0)
            fy = (dy > 0) - (dy < 0)
            if fx or fy:
                self.facing.update(fx, fy)

        self.pos.x += dx
        self.rect.topleft = self.pos
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                if dx < 0:
                    self.rect.left = wall.right
                self.pos.x = self.rect.x

        self.pos.y += dy
        self.rect.topleft = self.pos
        for wall in self.walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                if dy < 0:
                    self.rect.top = wall.bottom
                self.pos.y = self.rect.y


    def update(self):
        self.input()
