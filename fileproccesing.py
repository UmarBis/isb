import json
import argparse

class FileUtils:
    @staticmethod
    def read_bytes(path: str) -> bytes:
        """
        Чтение
        :param path: путь к файлу
        :return: чтение
        """
        try:
            with open(path, 'rb') as f:
                return f.read()
        except Exception as e:
            print("Error..", str(e))

    @staticmethod
    def write_bytes(path: str, data: bytes):
        """
        Запись
        :param path: путь для записи
        :param data: записываемые данные
        :return: запись
        """
        try:
            with open(path, 'wb') as f:
                f.write(data)
        except Exception as e:
            print("Error..", str(e))

    @staticmethod
    def load_config(path: str) -> dict:
        """
        Загрузка json
        :param path: путь к json
        :return: загрузка
        """
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("Error..", str(e))

    @staticmethod
    def argset():
        """
        Ввод аргументов через командную строку
        :return: аргументы
        """
        parser = argparse.ArgumentParser(description='Гибридная криптосистема с ChaCha20')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-gen', '--generation', action='store_true', help='Режим генерации ключей')
        group.add_argument('-enc', '--encryption', action='store_true', help='Режим шифрования')
        group.add_argument('-dec', '--decryption', action='store_true', help='Режим дешифрования')
        parser.add_argument('-c', '--config', help='Путь к файлу конфигурации', required=True)

        return parser.parse_args()
