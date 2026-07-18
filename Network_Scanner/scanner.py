from scapy.all import ARP, Ether, srp

def scan(ip_range):
    print(f"[*] جارٍ البحث عن الأجهزة في النطاق: {ip_range} ...")
    
    # ARP request حزمة لطلب معلومات الأجهزة
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # إرسال الحزمة وانتظار الردود (تم رفع الـ timeout لضمان التقاط جميع الأجهزة)
    result = srp(packet, timeout=5, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

# النطاق الخاص بك
target_ip = "192.168.0.1/24" 
devices = scan(target_ip)

print("-" * 50)
print(f"عدد الأجهزة المكتشفة: {len(devices)}")
print("-" * 50)
print(f"{'IP Address':<20} | {'MAC Address'}")
print("-" * 50)

for device in devices:
    print(f"{device['ip']:<20} | {device['mac']}")
