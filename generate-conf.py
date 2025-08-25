import socket
import os
import subprocess
import re
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
domains_file = os.path.join(script_dir, "domains.txt")
base_conf = os.path.join(script_dir, "base.conf")
output_conf = os.path.join(script_dir, "output.conf")
wireguard_exe = r"C:\Program Files\WireGuard\wireguard.exe"
interface_name = "output"

print(f"[INFO] Текущая директория: {script_dir}")

# Проверка файлов
if not os.path.exists(domains_file):
    print(f"[ERROR] Файл {domains_file} не найден.")
    sys.exit(1)
if not os.path.exists(base_conf):
    print(f"[ERROR] Файл {base_conf} не найден.")
    sys.exit(1)

# Читаем домены
print(f"[INFO] Чтение списка доменов из {domains_file}")
with open(domains_file, "r", encoding="utf-8") as f:
    domain_list = [line.strip() for line in f if line.strip()]

if not domain_list:
    print("[WARNING] Список доменов пуст.")
else:
    print(f"[INFO] Найдено {len(domain_list)} доменов")

ip_list = []

# Резолвим IP
for domain in domain_list:
    print(f"[INFO] Резолвинг {domain}...")
    try:
        ips = socket.getaddrinfo(domain, None, family=socket.AF_INET)
        for ip in {ip[4][0] for ip in ips}:
            ip_list.append(f"{ip}/32")
            print(f"[OK] {domain} -> {ip}")
    except socket.gaierror:
        print(f"[ERROR] Не удалось резолвить {domain}")

allowed_ips = ", ".join(ip_list)
print(f"[INFO] Список IP сформирован: {allowed_ips}")

# Замена в base.conf
print(f"[INFO] Обновление конфигурации {base_conf} -> {output_conf}")
with open(base_conf, "r", encoding="utf-8") as f:
    conf_text = f.read()

conf_text = re.sub(r"AllowedIPs\s*=\s*.*", f"AllowedIPs = {allowed_ips}", conf_text)

with open(output_conf, "w", encoding="utf-8") as f:
    f.write(conf_text)

print("[INFO] Конфигурация обновлена.")

print("\n✅ Генерация  завершены.")
