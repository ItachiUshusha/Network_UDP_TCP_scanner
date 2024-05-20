import socket

def scan_udp(host, port):
    # Создаем сокет для UDP соединения
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_s:
        # Устанавливаем время (тайм-аут)
        udp_s.settimeout(0.5)

        try:
            # Отправляем пустое сообщение
            udp_s.sendto(b"", (host, port))
            # Принимаем ответ
            data, adr = udp_s.recvfrom(1024)

            # Если получили ответ то выводим что порт открыт
            if adr:
                print(f"Порт {port} открыт.")
        # обрабатываем ошибку если истекло время
        except socket.timeout:
            print(f"Порт {port} открыт (тайм-аут истек)")
        # обрабатываем ошибку если порт закрыт
        except ConnectionResetError:
            #print(f"Не удалось поключиться к порту {port}")
            pass

        # закрываем сокет 👌
        udp_s.close()

host = ""

start = int(input("Введите с какого порта начать сканирование: "))
end = int(input("Введите до какого порта сканировать: "))

# Сканируем порты указанные пользователем
for port in range(start, end+1):
    scan_udp(host, port)
