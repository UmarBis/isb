import json
import argparse

def read_from_file(filename: str) -> str:
    """
    Чтение файла
    :param filename: имя файла
    :return: полученная строка из файла
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().strip()

def load_key(filename: str) -> str:
    """
    Загрузка ключа из json файла
    :param filename: файл с ключом
    :return: ключ
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def encrypt(text: str, key: str) -> str:
    """
    Шифрует текст с помощью ключа
    :param text: исходный текст
    :param key: ключ
    :return: зашифрованный ключ
    """
    return ''.join(key.get(char, char) for char in text.lower())

def write_file(encrypted_text: str) -> None:
    """
    Запись итогового текста в файл
    :param encrypted_text: итоговый текст
    :return: Запись
    """
    with open("task1_encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)

def main() -> None:
    parser = argparse.ArgumentParser(description='Processing images from a CSV file.')
    parser.add_argument('json_key', type=str, help='Path to the json.')
    parser.add_argument('input_text', type=str, help='Path to the input text.')
    args = parser.parse_args()


    key = load_key(args.json_key)

    original_text = read_from_file(args.input_text)
    encrypted_text = encrypt(original_text, key)

    try:
        write_file(encrypted_text)
        print("Исходный текст:", original_text)
        print("Зашифрованный текст:", encrypted_text)
        print("Запись/сохранение выполнено")
    except Exception as e:
        print("Ошибка при сохранении в файл:", str(e))

if __name__ == "__main__":
    main()