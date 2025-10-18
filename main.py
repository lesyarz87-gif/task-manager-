import requests
from datetime import datetime

def print_current_time():
    now = datetime.now()
    print(f"Текущее время: {now.strftime('%H:%M:%S')}")


def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print("✅ Интернет-соединение активно!")
        else:
            print("❌ Не удалось подключиться к интернету.")
    except requests.ConnectionError:
        print("❌ Ошибка соединения. Проверьте интернет.")

if __name__ == "__main__":
    print("Добро пожаловать в Task Manager!")
    print("=" * 40)
    print_current_time()
    check_internet_connection()
    print("Настройка окружения завершена успешно!")
