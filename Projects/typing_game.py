import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# إعداد الشاشة
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("من تصميم عدنان لعبة تحدي الكتابة - Kali")
font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

# تحميل الخلفية وتعديل حجمها
try:
    bg_image = pygame.image.load("bg.png")
    bg_image = pygame.transform.scale(bg_image, (800, 600))
except:
    bg_image = None

# قائمة الكلمات
word_list = ["python", "kali", "linux", "coding", "security", "hacker", "network", "firewall", "database", "variable", "function", "terminal", "script", "command", "server", "client", "encryption", "protocol", "binary", "system", "kernel", "memory", "storage", "cloud", "internet", "browser", "developer", "interface", "keyboard", "mouse", "monitor", "software", "hardware", "desktop", "laptop", "wireless", "bluetooth", "password", "username", "account", "login", "logout", "update", "install", "delete", "format", "render", "display", "graphic", "audio", "video", "music", "image", "vector", "pixel", "resolution", "speed", "logic", "syntax", "debug", "compile", "execute", "version", "patch", "exploit", "vulnerability", "threat", "malware", "virus", "spyware", "admin", "root", "sudo", "bash", "shell", "debian", "ubuntu", "fedora", "centos", "terminal"]

current_word = random.choice(word_list)
user_text = ""
score = 0

try:
    sound_correct = pygame.mixer.Sound("correct.mp3")
    sound_wrong = pygame.mixer.Sound("correct2.mp3")
except:
    pass

while True:
    # رسم الخلفية
    if bg_image:
        screen.blit(bg_image, (0, 0))
    else:
        screen.fill((20, 20, 20))
    
    color = (0, 255, 0) if current_word.startswith(user_text) else (255, 0, 0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                if user_text == current_word:
                    score += 10
                    sound_correct.play()
                    user_text = ""
                    current_word = random.choice(word_list)
                else:
                    sound_wrong.play()
                    user_text = ""
            else:
                user_text += event.unicode

    # رسم النصوص
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    target_text = font.render(f"Target: {current_word}", True, (255, 255, 255))
    input_text = font.render(f"Input: {user_text}", True, color)
    
    screen.blit(score_text, (600, 50))
    screen.blit(target_text, (50, 200))
    screen.blit(input_text, (50, 300))
    
    pygame.display.flip()
    clock.tick(30)
