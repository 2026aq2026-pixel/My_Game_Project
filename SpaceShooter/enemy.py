import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        # تحميل صورة الصاروخ
        self.image_orig = pygame.image.load('rocket.png').convert_alpha()
        self.image_orig = pygame.transform.scale(self.image_orig, (40, 50))
        
        # إنشاء نسخة لصبغها باللون
        self.image = self.image_orig.copy()
        
        # قائمة الألوان التي ستغير مظهر الصاروخ حسب المرحلة
        colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
        color = colors[level % len(colors)]
        
        # "صبغ" الصاروخ باللون المحدد
        self.image.fill(color, special_flags=pygame.BLEND_RGB_MULT)
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self.rect.y = random.randint(-150, -50)
        
        # زيادة السرعة تدريجياً
        self.speedy = random.randint(3, 6 + (level // 2))

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > 600:
            self.kill()
