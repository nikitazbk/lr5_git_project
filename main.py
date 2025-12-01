# main.py - Простой сканер безопасности (учебный пример)

import socket

def check_port(host, port):
    """
    Проверяет, открыт ли порт на указанном хосте.
    Возвращает True, если порт открыт (слушает).
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Таймаут 1 секунда
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

if __name__ == "__main__":
    print("=== Учебный сканер портов ===")
    target_host = "127.0.0.1" # Локальный хост для безопасного тестирования
    
    # Список часто используемых портов для проверки
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3389]

    print(f"Сканирую хост {target_host} на предмет открытых портов...")
    for port in common_ports:
        if check_port(target_host, port):
            print(f"[!] Порт {port} ОТКРЫТ")
        else:
            print(f"[ ] Порт {port} закрыт")
    print("Сканирование завершено.")