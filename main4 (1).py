import csv
import json
import os

def convert_csv_to_json(csv_file, json_file):
    """
    Конвертує дані з CSV у JSON.
    Приймає шлях до вхідного та вихідного файлів.
    """
    data = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f_csv:
            csv_reader = csv.DictReader(f_csv)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Помилка: файл '{csv_file}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні CSV-файлу: {e}")
        return

    try:
        with open(json_file, 'w', encoding='utf-8') as f_json:
            json.dump(data, f_json, indent=4)
        print(f"Дані успішно конвертовано з '{csv_file}' у '{json_file}'.")
    except Exception as e:
        print(f"Помилка при записі у JSON-файл: {e}")

def convert_json_to_csv(json_file, csv_file, new_data=[]):
    """
    Конвертує дані з JSON у CSV та додає нові рядки.
    Приймає шлях до вхідного та вихідного файлів, а також нові дані.
    """
    data = []
    try:
        with open(json_file, 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
    except FileNotFoundError:
        print(f"Помилка: файл '{json_file}' не знайдено.")
        return
    except json.JSONDecodeError:
        print(f"Помилка: файл '{json_file}' має некоректний формат JSON.")
        return
    except Exception as e:
        print(f"Помилка при читанні JSON-файлу: {e}")
        return

    data.extend(new_data)
    
    if not data:
        print("Немає даних для запису.")
        return
    headers = data[0].keys()

    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as f_csv:
            csv_writer = csv.DictWriter(f_csv, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        print(f"Дані успішно конвертовано з '{json_file}' у '{csv_file}'.")
    except Exception as e:
        print(f"Помилка при записі у CSV-файл: {e}")

def student_1_task():
    """
    Студент 1: Ковальчук
    Створює CSV файл та конвертує його в JSON.
    """
    print("\n--- Завдання Студента 1 ---")
    file_content = [
        {'id': '1', 'name': 'Іван Ковальчук', 'age': '20', 'city': 'Київ'},
        {'id': '2', 'name': 'Марія Мельник', 'age': '22', 'city': 'Львів'}
    ]
    try:
        with open('data.csv', 'w', encoding='utf-8', newline='') as f:
            headers = file_content[0].keys()
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(file_content)
        print("Файл 'data.csv' створено та заповнено.")
        convert_csv_to_json('data.csv', 'data.json')
    except Exception as e:
        print(f"Помилка при виконанні завдання Студента 1: {e}")

def student_2_task():
    """
    Студент 2: Петренко
    Конвертує JSON в CSV, додаючи нові рядки.
    """
    print("\n--- Завдання Студента 2 ---")
    new_rows = [
        {'id': '3', 'name': 'Олександр Петренко', 'age': '21', 'city': 'Харків'},
        {'id': '4', 'name': 'Наталія Бойко', 'age': '19', 'city': 'Одеса'}
    ]
    convert_json_to_csv('data.json', 'data.csv', new_rows)

def student_3_task():
    """
    Студент 3: Мельник
    Конвертує CSV в JSON, додаючи нові рядки.
    """
    print("\n--- Завдання Студента 3 ---")
    data = []
    try:
        with open('data.csv', 'r', encoding='utf-8') as f_csv:
            csv_reader = csv.DictReader(f_csv)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("Помилка: файл 'data.csv' не знайдено.")
        return

    new_rows = [
        {'id': '5', 'name': 'Вікторія Іваненко', 'age': '23', 'city': 'Дніпро'}
    ]
    data.extend(new_rows)
    
    try:
        with open('data.json', 'w', encoding='utf-8') as f_json:
            json.dump(data, f_json, indent=4)
        print(f"Дані успішно оновлено та конвертовано з 'data.csv' у 'data.json'.")
    except Exception as e:
        print(f"Помилка при записі у JSON-файл: {e}")

if __name__ == "__main__":
    student_1_task()
    student_2_task()
    student_3_task()