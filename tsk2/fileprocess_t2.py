import json
import argparse

def argset():
    """
    Ввод аргументов через командную строку
    :return: аргументы
    """
    parser = argparse.ArgumentParser(description='Processing images from a CSV file.')
    parser.add_argument('enc_text', type=str, help='Path to the enc text.')
    parser.add_argument('output_textfile', type=str, help='Path for saving text.')
    parser.add_argument('output_keyfile', type=str, help='Path for saving key.')
    parser.add_argument('rus_freq', type=str, help='Path to rus freq.')
    args = parser.parse_args()
    return args




def write_to_file(decryption_key, output_keyfile: str) -> None:
    """
    Запись ключа в файл
    :param decryption_key: ключ дешифрования
    :return: запись
    """
    try:
        with open(output_keyfile, "w", encoding="utf-8") as file:
            json.dump(decryption_key, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Ошибка при записи: ", str(e))

def load_freq(filename: str) -> str:
    """
    Загрузка частот из json файла
    :param filename: файл с частотами
    :return: частоты
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print("Ошибка при чтении частот алфавита.")
