from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class RSACipher:
    @staticmethod
    def generate_keys():
        """
        Генерация ключей
        :return: (приватный ключ, публичный ключ)
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def encrypt(data: bytes, public_key) -> bytes:
        """
        Шифрование данных
        :param data: данные
        :param public_key: открытый ключ
        :return: их шифр
        """
        return public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt(encrypted_data: bytes, private_key) -> bytes:
        """
        Дешифрование данных
        :param encrypted_data: зашифрованные данные
        :param private_key: закрытый ключ
        :return: расшифрованные данные
        """
        return private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def save_keys(private_key, private_key_path: str, public_key_path: str):
        """
        Сохранение ключей
        :param private_key: приватный ключ
        :param private_key_path: путь к файлу приватного ключа
        :param public_key_path: путь к файлу публичного ключа
        :return: сохранение на диск
        """
        with open(private_key_path, 'wb') as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        public_key = private_key.public_key()
        with open(public_key_path, 'wb') as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    @staticmethod
    def load_private_key(path: str):
        """
        Загрузка приватного ключа
        :param path: путь к приватному ключу
        :return: приватный ключ
        """
        with open(path, 'rb') as f:
            return serialization.load_pem_private_key(
                f.read(),
                password=None
            )

    @staticmethod
    def load_public_key(path: str):
        """
        Загрузка публичного ключа
        :param path: путь к публичному ключу
        :return: публичный ключ
        """
        with open(path, 'rb') as f:
            return serialization.load_pem_public_key(f.read())
