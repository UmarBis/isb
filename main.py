from hybrid import HybridCipher
from fileproccesing import FileUtils


def main():
    args = FileUtils.argset()

    try:
        config = FileUtils.load_config(args.config)
        cipher = HybridCipher()

        if args.generation:
            print("Генерация ключей...")
            cipher.generate_keys(
                config['symmetric_key_path'],
                config['public_key_path'],
                config['private_key_path']
            )
            print("Генерация ключей завершена!")

        elif args.encryption:
            print("Шифрование файла...")
            cipher.encrypt_file(
                config['input_file_path'],
                config['encrypted_file_path'],
                config['private_key_path'],
                config['symmetric_key_path']
            )
            print("Шифрование завершено!")

        else:
            print("Дешифрование файла...")
            cipher.decrypt_file(
                config['encrypted_file_path'],
                config['decrypted_file_path'],
                config['private_key_path'],
                config['symmetric_key_path']
            )
            print("Дешифрование завершено!")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    main()