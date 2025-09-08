import re

def generate_source_file():
    input_data = """Це приклад, який демонструє, як; слова! можуть? бути.
Розділені, різними, розділовими знаками!
Ось ще один, рядок з: текстом; для перевірки..."""
    
    with open('TF1_1.txt', 'w', encoding='utf-8') as file_a:
        file_a.write(input_data)

def process_and_create_target_file():
    try:
        with open('TF1_1.txt', 'r', encoding='utf-8') as source_file:
            raw_text = source_file.read()
    except FileNotFoundError:
        return

    processed_text = re.sub(r'[.,;!?:…—]', ' ', raw_text)
    
    word_list = [word for word in processed_text.split() if word]

    with open('TF1_2.txt', 'w', encoding='utf-8') as target_file:
        for single_word in word_list:
            target_file.write(single_word + '\n')

def display_target_file_content():
    try:
        with open('TF1_2.txt', 'r', encoding='utf-8') as final_file:
            for line in final_file:
                print(line.strip())
    except FileNotFoundError:
        return

if __name__ == "__main__":
    generate_source_file()
    process_and_create_target_file()
    display_target_file_content()