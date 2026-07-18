import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, bullets, all_sprites):
        super().__init__()
        self.image = pygame.image.load('shps.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800: self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0: self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600: self.rect.y += self.speed

    def shoot(self):
        b = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(b)
        self.bullets.add(b)
