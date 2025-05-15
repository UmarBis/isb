from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import os


class ChaCha20Cipher:
    def __init__(self):
        self.key = None
        self.nonce = None

    def generate_key(self, config):
        """
        Генерация ключа и nonce (Chacha20)
        :param config: конфиг 
        :return: key & nonce
        """
        s1 = config["s1"]
        s2 = config["s2"]
        self.key = os.urandom(s1)
        self.nonce = os.urandom(s2)
        return self.key + self.nonce

    def encrypt(self, data: bytes) -> bytes:
        """
        Шифрование данных
        :param data: данные
        :return: их шифр
        """
        if not self.key or not self.nonce:
            raise ValueError("Ключ не инициализирован")

        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None)
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize()

    def decrypt(self, data: bytes) -> bytes:
        """
        Дешифрование данных
        :param data: шифрованные данные
        :return: их дешифр
        """
        if not self.key or not self.nonce:
            raise ValueError("Ключ не инициализирован")

        cipher = Cipher(algorithms.ChaCha20(self.key, self.nonce), mode=None)
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()

    def set_key(self, key_data: bytes):
        """
        Установка key & nonce
        :param key_data: данные
        :return: их установка
        """
        if len(key_data) != 48:
            raise ValueError("Неверная длина ключа")
        self.key = key_data[:32]
        self.nonce = key_data[32:]
