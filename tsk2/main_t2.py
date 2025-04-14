from isb.lab_1.tsk2.cipher_t2 import comp_key, decrypt_text
from isb.lab_1.tsk2.fileprocess_t2 import read_file, write_to_file, load_freq, argset

def main() -> None:
    args = argset()

    rus_freq = load_freq(args.rus_freq)

    encrypted_text = read_file(args.enc_text)
    decryption_key = comp_key(encrypted_text, rus_freq)
    decrypted_text = decrypt_text(encrypted_text, decryption_key)
    try:
        write_to_file(decrypted_text, args.output_textfile, decryption_key, args.output_keyfile)
        print("Дешифрование завершено!")
        print("Результаты сохранены в файлы...")
    except Exception as e:
        print("Произошла ошибка при сохранении/записи текста:", str(e))

if __name__ == "__main__":
    main()