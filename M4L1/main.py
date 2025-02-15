import schedule
import time

# Функция, которую нужно выполнить по расписанию
def my_task():
    print("Выполняю задачу...")

# Запланировать выполнение задачи каждую минуту
schedule.every(1).minutes.do(my_task)

# Цикл планирования
while True:
    schedule.run_pending()
    time.sleep(1)  # Пауза в 1 секунду