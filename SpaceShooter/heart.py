import pygame
import random

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # رسم قلب بسيط (دائرتان ومثلث) أو يمكنك استخدام صورة لو توفرت
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 8)
        pygame.draw.circle(self.image, (255, 0, 0), (20, 10), 8)
        pygame.draw.polygon(self.image, (255, 0, 0), [(3, 15), (27, 15), (15, 28)])
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 770)
        self.rect.y = -50
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > 600: self.kill()
