import pygame
from assets import load_img
from map import in_bounds
from tools import use_tool

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, tilesize, walls):
        super().__init__()
        self.image = load_img("player_d0", (tilesize, tilesize))
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 2
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.walls = walls
        self.facing = pygame.math.Vector2(0, 1)
        self.tool = 1
        self.tilesize = tilesize

    def handle_event(self, event, tilesize):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0: self.tool = 0
            elif event.key == pygame.K_1: self.tool = 1
            elif event.key == pygame.K_2: self.tool = 2
            elif event.key == pygame.K_3: self.tool = 3
            elif event.key == pygame.K_4: self.tool = 4
            elif event.key == pygame.K_5: self.tool = 5
            elif event.key == pygame.K_6: self.tool = 6
            elif event.key == pygame.K_7: self.tool = 7
            elif event.key == pygame.K_8: self.tool = 8
            elif event.key == pygame.K_9: self.tool = 9
            elif event.key == pygame.K_SPACE:
                cx, cy = self.rect.center
                px, py = cx // tilesize, cy // tilesize
                fx, fy = int(self.facing.x), int(self.facing.y)
                tx, ty = px + fx, py + fy
                if in_bounds(tx, ty):
                    use_tool(self.tool, tx, ty)

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