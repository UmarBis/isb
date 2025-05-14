import argparse
import json 

def argset():
    """
    Ввод аргументов через командную строку
    :return: аргументы
    """
    parser = argparse.ArgumentParser(description='Processing images from a CSV file.')
    parser.add_argument('file', type=str, help='Path to the input text.')
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
        print("Error..", str(e))

def read_json(filename: str) -> str:
    """
    Чтение файла
    :param filename: имя файла
    :return: значения оттуда 
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print("Error..", str(e))
