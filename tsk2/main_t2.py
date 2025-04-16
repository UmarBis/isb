from isb.lab_1.tsk2.cipher_t2 import comp_key, decrypt_text
from isb.lab_1.tsk2.fileprocess_t2 import write_to_file, load_freq, argset
from isb.lab_1.tsk1.fileprocess_t1 import read_from_file, write_file
def main() -> None:
    args = argset()

    rus_freq = load_freq(args.rus_freq)

    encrypted_text = read_from_file(args.enc_text)
    decryption_key = comp_key(encrypted_text, rus_freq)
    decrypted_text = decrypt_text(encrypted_text, decryption_key)

    write_file(decrypted_text, args.output_textfile)
    write_to_file(decryption_key, args.output_keyfile)
    print("Дешифрование завершено!")
    print("Результаты сохранены в файлы...")

if __name__ == "__main__":
    main()
