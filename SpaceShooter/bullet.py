import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # تحميل صورة الليزر من المجلد الرئيسي
        self.image = pygame.image.load('rocket.png').convert_alpha()
        
        # تغيير حجم الصورة إذا كانت غير مناسبة
        self.image = pygame.transform.scale(self.image, (20, 40))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        # حذف الرصاصة إذا خرجت من الشاشة
        if self.rect.bottom < 0:
            self.kill()
