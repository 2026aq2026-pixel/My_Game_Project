import pygame
import psutil
import subprocess
import os

# تهيئة pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Kali System Monitor & Network Scanner")

# الألوان والخطوط
KALI_GREEN = (0, 255, 65)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("monospace", 16, bold=True)
clock = pygame.time.Clock()

def get_connected_devices():
    """تنفيذ أمر arp-scan وجلب النتائج"""
    try:
        output = subprocess.check_output(["sudo", "arp-scan", "-l"]).decode('utf-8')
        lines = output.split('\n')
        devices = []
        for line in lines:
            if "192.168" in line:
                devices.append(line.strip())
        return devices[:10]
    except:
        return ["Error scanning network"]

def save_devices_to_log(devices):
    """حفظ الأجهزة المكتشفة في ملف نصي بمسار ثابت"""
    log_path = "/home/kali/Desktop/My_Work_Link/Notes/network_log.txt"
    
    with open(log_path, "a") as f:
        f.write("\n--- Scan Results ---\n")
        for dev in devices:
            f.write(dev + "\n")

running = True
counter = 0 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # رسم الإطار الخارجي
    pygame.draw.rect(screen, KALI_GREEN, (10, 10, 780, 580), 3)

    # عرض بيانات النظام
    cpu_text = font.render(f"CPU LOAD: {psutil.cpu_percent()}%", True, KALI_GREEN)
    ram_text = font.render(f"RAM USAGE: {psutil.virtual_memory().percent}%", True, KALI_GREEN)
    screen.blit(cpu_text, (50, 50))
    screen.blit(ram_text, (50, 80))

    # عرض قائمة الأجهزة
    header = font.render("> CONNECTED DEVICES:", True, KALI_GREEN)
    screen.blit(header, (50, 130))
    
    devices = get_connected_devices()
    
    # حفظ النتائج في الملف
    if counter % 50 == 0: 
        if devices and "Error" not in devices[0]:
            save_devices_to_log(devices)

    for i, dev in enumerate(devices):
        dev_text = font.render(dev, True, KALI_GREEN)
        screen.blit(dev_text, (50, 160 + (i * 30)))

    pygame.display.flip()
    clock.tick(10)
    counter += 1

pygame.quit()
