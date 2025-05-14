from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """
        Генерация ключей
        :return: ключи
        """
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def encrypt(self, data: bytes) -> bytes:
        """
        Шифрование данных
        :param data: данные
        :return: их шифр
        """
        if not self.public_key:
            raise ValueError("Ключи не инициализированы")

        return self.public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def decrypt(self, encrypted_data: bytes) -> bytes:
        """
        Дешифрование данных
        :param encrypted_data: шифрованные данные
        :return: их дешифр
        """
        if not self.private_key:
            raise ValueError("Закрытый ключ не инициализирован")

        return self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def load_keys(self, private_key_path: str, public_key_path: str):
        """
        Загрузка ключей
        :param private_key_path: приватный ключ
        :param public_key_path: публичный ключ
        :return: их загрузка
        """
        with open(private_key_path, 'rb') as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_key_path: str, public_key_path: str):
        """
        Сохранение ключей
        :param private_key_path: приватный ключ
        :param public_key_path: публичный ключ
        :return: их сохранение
        """
        if not self.private_key or not self.public_key:
            raise ValueError("Ключи не инициализированы")

        with open(private_key_path, 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open(public_key_path, 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))