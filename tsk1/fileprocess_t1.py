import json
import argparse

def argset():
    """
    Ввод аргументов через командную строку
    :return: аргументы
    """
    parser = argparse.ArgumentParser(description='Processing images from a CSV file.')
    parser.add_argument('json_key', type=str, help='Path to the json.')
    parser.add_argument('input_text', type=str, help='Path to the input text.')
    parser.add_argument('output_file', type=str, help='Path to the input text.')
    args = parser.parse_args()
    return args

def read_from_file(filename: str) -> str:
    """
    Чтение файла
    :param filename: имя файла
    :return: полученная строка из файла
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print("Не удалось прочесть файл: ", str(e))

def load_key(filename: str) -> str:
    """
    Загрузка ключа из json файла
    :param filename: файл с ключом
    :return: ключ
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Ошибка при загрузке ключа: ", str(e))


def write_file(encrypted_text: str, filename) -> None:
    """
    Запись итогового текста в файл
    :param encrypted_text: итоговый текст
    :return: Запись
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(encrypted_text)
    except Exception as e:
        print("Ошибка при записи: ", str(e))
