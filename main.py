# main.py - Простой сканер безопасности (учебный пример)
# Лабораторная работа №5

import socket

def check_port(host, port):
    """
    Проверяет, открыт ли порт на указанном хосте.
    Возвращает True, если порт открыт.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def get_service_name(port):
    """
    Определяет сервис по номеру порта.
    Например: порт 80 → "HTTP", порт 443 → "HTTPS"
    """
    services = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3389: "RDP"
    }
    return services.get(port, "Неизвестно")

if __name__ == "__main__":
    print("=== Сканер портов ===")
    target_host = "127.0.0.1"  # Сканируем свой же компьютер (безопасно)
    
    # Проверяем эти порты:
    common_ports = [21, 22, 80, 443, 3389]
    
    print(f"Сканирую {target_host}...")
    for port in common_ports:
        is_open = check_port(target_host, port)
        service = get_service_name(port)  # Используем новую функцию
        if is_open:
            print(f"[!] Порт {port} ({service}): ОТКРЫТ")
        else:
            print(f"[ ] Порт {port} ({service}): закрыт")
    print("Готово!")