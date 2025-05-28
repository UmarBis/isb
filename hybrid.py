from symmetr import ChaCha20Cipher
from asymmetr import RSACipher
from fileproccesing import FileUtils


class HybridCipher:
    def __init__(self):
        self.symmetric = ChaCha20Cipher()


    def generate_keys(self, symmetric_key_path: str, public_key_path: str, private_key_path: str):
        """
        Генерация всех ключей
        :param symmetric_key_path: путь к симметричному ключу
        :param public_key_path: путь к публичному ключу
        :param private_key_path: путь к приватному ключу
        :return: шифрование и сохранение симметричного ключа
        """
        symmetric_key_data = self.symmetric.generate_key()

        self.asymmetric.generate_keys()

        self.asymmetric.save_keys(private_key_path, public_key_path)

        encrypted_sym_key = self.asymmetric.encrypt(symmetric_key_data)
        FileUtils.write_bytes(symmetric_key_path, encrypted_sym_key)

    def encrypt_file(self, input_path: str, output_path: str, private_key_path: str,
                     encrypted_sym_key_path: str):
        """
        Шифрование файла
        :param input_path: входные данные
        :param output_path: выходные данные
        :param private_key_path: приватный ключ
        :param encrypted_sym_key_path: зашифрованный симметричный ключ
        :return: шифр файла
        """
        self.asymmetric.load_keys(private_key_path, None)

        encrypted_sym_key = FileUtils.read_bytes(encrypted_sym_key_path)
        symmetric_key_data = self.asymmetric.decrypt(encrypted_sym_key)
        self.symmetric.set_key(symmetric_key_data)

        data = FileUtils.read_bytes(input_path)
        encrypted_data = self.symmetric.encrypt(data)
        FileUtils.write_bytes(output_path, encrypted_data)

    def decrypt_file(self, input_path: str, output_path: str, private_key_path: str,
                     encrypted_sym_key_path: str):
        """
        Дешифрование файла
        :param input_path: входное
        :param output_path: выходное
        :param private_key_path: приватный ключ
        :param encrypted_sym_key_path: зашифрованный симметричный ключ
        :return: дешифр файла
        """
        self.asymmetric.load_keys(private_key_path, None)

        encrypted_sym_key = FileUtils.read_bytes(encrypted_sym_key_path)
        symmetric_key_data = self.asymmetric.decrypt(encrypted_sym_key)
        self.symmetric.set_key(symmetric_key_data)

        encrypted_data = FileUtils.read_bytes(input_path)
        decrypted_data = self.symmetric.decrypt(encrypted_data)
        FileUtils.write_bytes(output_path, decrypted_data)
