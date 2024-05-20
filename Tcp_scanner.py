import socket

def scan_ports(host, start_port, end_port):
    # Проходим по всем портам в заданном диапазоне
    for port in range(start_port, end_port + 1):
        # Создаем сокет для TCP соединения
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)  # Устанавливаем таймаут в 0.5 секунд

        # Пытаемся установить TCP соединение с целевым хостом и портом
        result = sock.connect_ex((host, port))

        # Проверяем, открыт ли порт
        if result == 0:
            print(f"Порт {port} открыт")
        else:
            print(f"Порт {port} закрыт")

        # Закрываем сокет 👌
        sock.close()


host = ""  # Целевой хост
start_port = int(input("Введите с какого порта начать сканирование: "))  # Стартовый порт
end_port = int(input("Введите до какого порта сканировать: "))  # Конечный порт

scan_ports(host, start_port, end_port)
