import pygame
import random
from player import Player
from bullet import Bullet
from enemy import Enemy
from heart import Heart

# إعدادات النظام
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter Pro")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)
font_big = pygame.font.SysFont("Arial", 50)

# تحميل الملفات
bg_img = pygame.image.load('adssa.jpg').convert()
bg_img = pygame.transform.scale(bg_img, (800, 600))
bg_y1, bg_y2 = 0, -600

# 1. تحميل وتجهيز الشعار
logo = pygame.image.load('acacw.png').convert_alpha()
logo = pygame.transform.scale(logo, (150, 150)) # تصغير الحجم قليلاً ليكون مناسباً للأعلى

# صبغ الشعار باللون الأبيض
logo.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_MULT)

# ضبط الشفافية
logo.set_alpha(150) 

# 2. رسم الشعار (في حلقة while، بعد رسم الخلفية)
screen.blit(bg_img, (0, bg_y1))
screen.blit(bg_img, (0, bg_y2))

# تغيير الإحداثيات هنا لنقله للأعلى
# (325, 20) تعني في منتصف العرض (800/2 - 75) وعلى مسافة 20 بكسل من الأعلى
screen.blit(logo, (325, 10))

shoot_sound = pygame.mixer.Sound('sounds/sond11.mp3')
explosion_sound = pygame.mixer.Sound('sounds/sond10.mp3')

# المتغيرات الأساسية
level = 1
score = 0
lives = 3
game_over = False
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
hearts = pygame.sprite.Group()

player = Player(bullets, all_sprites)
all_sprites.add(player)

running = True
while running:
    # 1. شاشة النهاية
    if game_over:
        screen.fill((0, 0, 0))
        msg = font_big.render("GAME OVER - Press R to Restart", True, (255, 255, 255))
        screen.blit(msg, (80, 250))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                lives = 3; score = 0; level = 1; game_over = False
                all_sprites.empty(); enemies.empty(); bullets.empty(); hearts.empty()
                player = Player(bullets, all_sprites)
                all_sprites.add(player)
        continue

    # 2. منطق اللعبة
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.shoot()
            shoot_sound.play()

    if score >= level * 100 and level < 30: level += 1

    if random.randint(1, max(5, 40 - level)) == 1:
        e = Enemy(level)
        all_sprites.add(e)
        enemies.add(e)

    if random.randint(1, 1000) == 1:
        h = Heart()
        all_sprites.add(h)
        hearts.add(h)

    # التصادمات
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 10
        explosion_sound.play()

    if pygame.sprite.spritecollide(player, enemies, True):
        lives -= 1
        explosion_sound.play()
        if lives <= 0: game_over = True

    if pygame.sprite.spritecollide(player, hearts, True):
        lives += 1

    # تحديث الخلفية والرسم
    bg_y1 += 2; bg_y2 += 2
    if bg_y1 >= 600: bg_y1 = -600
    if bg_y2 >= 600: bg_y2 = -600
    
    all_sprites.update()
    screen.blit(bg_img, (0, bg_y1))
    screen.blit(bg_img, (0, bg_y2))
    screen.blit(logo, (325, 20)) # رسم العلامة المائية
    all_sprites.draw(screen)
    
    status_text = font.render(f"Level: {level} | Lives: {lives} | Score: {score}", True, (255, 255, 255))
    screen.blit(status_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
