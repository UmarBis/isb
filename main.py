from hybrid import HybridCipher
from fileproccesing import FileUtils
from enum import Enum

class Mode(Enum):
    GENERATION = "generation"
    ENCRYPTION = "encryption"
    DECRYPTION = "decryption"
    
def main():
    args = FileUtils.argset()

    try:
        config = FileUtils.load_config(args.config)
        cipher = HybridCipher()

        mode_map = {
            True: Mode.GENERATION,
            False: Mode.ENCRYPTION if args.encryption else Mode.DECRYPTION
        }
        mode = mode_map[args.generation]
        
        match mode:
            case Mode.GENERATION:
                print("Генерация ключей...")
                cipher.generate_keys(
                    config['symmetric_key_path'],
                    config['public_key_path'],
                    config['private_key_path']
                )
                print("Генерация ключей завершена!")
    
            case Mode.ENCRYPTION:
                print("Шифрование файла...")
                cipher.encrypt_file(
                    config['input_file_path'],
                    config['encrypted_file_path'],
                    config['private_key_path'],
                    config['symmetric_key_path']
                )
                print("Шифрование завершено!")
    
            case Mode.DECRYPTION:
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
