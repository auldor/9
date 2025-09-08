import os

def student_1_task():
    """Створює файл, записує прізвище та питання."""
    try:
        with open('communication.txt', 'w', encoding='utf-8') as f:
            f.write("Ковальчук\n")
            f.write("Питання: Як обробляти виняткові ситуації при роботі з файлами в Python?\n")
        print("Завдання Студента 1 виконано успішно.")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")

def student_2_task():
    """Записує прізвище, відповідь і нове питання."""
    try:
        with open('communication.txt', 'a', encoding='utf-8') as f:
            f.write("\n\nМельник\n")
            f.write("Відповідь: Для обробки винятків використовується блок try-except. Код, який може спричинити помилку, поміщається в блок try. Якщо виникає помилка, управління передається в блок except, де можна обробити цю помилку, наприклад, вивести повідомлення.\n")
            f.write("Питання: Які основні режими відкриття файлів у Python і для чого вони потрібні?\n")
        print("Завдання Студента 2 виконано успішно.")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")

def student_3_task():
    """Записує прізвище, відповідь і нове питання."""
    try:
        with open('communication.txt', 'a', encoding='utf-8') as f:
            f.write("\n\nПетренко\n")
            f.write("Відповідь: Основні режими: 'r' (читання), 'w' (запис, перезаписує файл), 'a' (дозапис, додає дані в кінець файлу). Також є бінарні режими 'rb', 'wb', 'ab' для роботи з нетекстовими даними.\n")
            f.write("Питання: Яка різниця між методами close() та використанням with open(...)?\n")
        print("Завдання Студента 3 виконано успішно.")
    except IOError as e:
        print(f"Помилка при роботі з файлом: {e}")

def read_and_print_file(filename="communication.txt"):
    """Читає та виводить вміст файлу у консоль."""
    try:
        if not os.path.exists(filename):
            print(f"Файл '{filename}' не знайдено.")
            return

        print("\n--- Повний вміст файлу ---\n")
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
        print("--------------------------\n")
    except IOError as e:
        print(f"Помилка при читанні файлу: {e}")

if __name__ == "__main__":
    student_1_task()
    student_2_task()
    student_3_task()
    read_and_print_file()