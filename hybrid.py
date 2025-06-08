from symmetr import ChaCha20Cipher
from asymmetr import RSACipher
from fileproccesing import FileUtils


class HybridCipher:
    def __init__(self):
        pass
        
    def generate_keys(self, symmetric_key_path: str, public_key_path: str, private_key_path: str):
        """
        Генерация всех ключей
        :param symmetric_key_path: путь к симметричному ключу
        :param public_key_path: путь к публичному ключу
        :param private_key_path: путь к приватному ключу
        :return: шифрование и сохранение симметричного ключа
        """
        symmetric_cipher = ChaCha20Cipher()
        symmetric_key_data = symmetric_cipher.generate_key()

        private_key, public_key = RSACipher.generate_keys()
        RSACipher.save_keys(private_key, private_key_path, public_key_path)

        encrypted_key = RSACipher.encrypt(public_key, symmetric_key_data)
        FileUtils.write_bytes(symmetric_key_path, encrypted_key)

    def encrypt_file(self, input_path: str, output_path: str,
                     private_key_path: str, encrypted_sym_key_path: str):
        """
        Шифрование файла
        :param input_path: путь к исходному файлу
        :param output_path: путь к зашифрованному файлу
        :param private_key_path: путь к приватному ключу
        :param encrypted_sym_key_path: путь к зашифрованному симметричному ключу
        :return: шифрование и сохранение файла
        """

        private_key = RSACipher.load_private_key(private_key_path)
        encrypted_sym_key = FileUtils.read_bytes(encrypted_sym_key_path)
        symmetric_key_data = RSACipher.decrypt(private_key, encrypted_sym_key)

        symmetric_cipher = ChaCha20Cipher()
        symmetric_cipher.set_key(symmetric_key_data)

        plaintext = FileUtils.read_bytes(input_path)
        encrypted = symmetric_cipher.encrypt(plaintext)
        FileUtils.write_bytes(output_path, encrypted)

    def decrypt_file(self, input_path: str, output_path: str,
                     private_key_path: str, encrypted_sym_key_path: str):
        """
        Дешифрование файла
        :param input_path: путь к зашифрованному файлу
        :param output_path: путь к расшифрованному файлу
        :param private_key_path: путь к приватному ключу
        :param encrypted_sym_key_path: путь к зашифрованному симметричному ключу
        :return: восстановление исходного файла
        """

        private_key = RSACipher.load_private_key(private_key_path)
        encrypted_sym_key = FileUtils.read_bytes(encrypted_sym_key_path)
        symmetric_key_data = RSACipher.decrypt(private_key, encrypted_sym_key)

        symmetric_cipher = ChaCha20Cipher()
        symmetric_cipher.set_key(symmetric_key_data)

        encrypted_data = FileUtils.read_bytes(input_path)
        decrypted_data = symmetric_cipher.decrypt(encrypted_data)
        FileUtils.write_bytes(output_path, decrypted_data)
