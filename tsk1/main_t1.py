from isb.lab_1.tsk1.fileprocess_t1 import read_from_file, load_key, write_file, argset
from isb.lab_1.tsk1.cipher_t1 import encrypt


def main() -> None:
    args = argset()
    key = load_key(args.json_key)
    original_text = read_from_file(args.input_text)


    encrypted_text = encrypt(original_text, key)

    try:
        write_file(encrypted_text, args.output_file)
        print("Исходный текст:", original_text)
        print("Зашифрованный текст:", encrypted_text)
        print("Запись/сохранение выполнено")
    except Exception as e:
        print("Ошибка при сохранении в файл:", str(e))

if __name__ == "__main__":
    main()