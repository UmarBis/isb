import json
from collections import Counter
import argparse

def read_file(filename: str) -> str:
    """
    Чтение файла
    :param filename: имя файла
    :return: прочитанная строка из файла
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def comp_key(encrypted_text: str):
    """
    Построение ключа путем сопоставления посчитанных частот символов
    :param encrypted_text: зашифрованный текст
    :return: готовый ключ
    """
    rus_frq = {
        ' ': 0.128675, 'о': 0.096456, 'и': 0.075312, 'е': 0.072292, 'а': 0.064841,
        'н': 0.061820, 'т': 0.061619, 'с': 0.051953, 'р': 0.040677, 'в': 0.039267,
        'м': 0.029803, 'л': 0.029400, 'д': 0.026983, 'я': 0.026379, 'к': 0.025977,
        'п': 0.024768, 'з': 0.015908, 'ы': 0.015707, 'ь': 0.015103, 'у': 0.013290,
        'ч': 0.011679, 'ж': 0.010673, 'г': 0.009867, 'х': 0.008659, 'ф': 0.007249,
        'й': 0.006847, 'ю': 0.006847, 'б': 0.006645, 'ц': 0.005034, 'ш': 0.004229,
        'щ': 0.003625, 'э': 0.002416, 'ъ': 0.000000
    }
    total_chars = len(encrypted_text)
    char_counts = Counter(encrypted_text)
    char_freq = {char: count / total_chars for char, count in char_counts.items()}

    print("\nЧастоты зашифрованного текста:\n")
    for char, freq in sorted(char_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"'{char}': {freq:.6f}")
    # Сортируем символы по убыванию частоты
    sorted_encrypted_chars = sorted(char_freq, key=char_freq.get, reverse=True)
    sorted_russian_chars = sorted(rus_frq, key=rus_frq.get, reverse=True)
    # Создаем таблицу подстановки, сопоставляя частоты
    decryption_key = {enc: rus for enc, rus in zip(sorted_encrypted_chars, sorted_russian_chars)}
    return decryption_key

def decrypt_text(enc_text: str, decryption_key:str) -> str:
    """
    Дешифрование текста при помощи полученного ключа
    :param enc_text: зашифрованный текст
    :param decryption_key: полученный ключ
    :return: дешифрованный текст
    """
    decrypted_text = "".join(decryption_key.get(char, char) for char in enc_text)
    return decrypted_text


def write_to_file(decrypted_text: str, decryption_key) -> None:
    """
    Запись текста и ключа в файл
    :param decrypted_text: дешифрованный текст
    :param decryption_key: ключ дешифрования
    :return: запись
    """
    with open("task2_decrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(decrypted_text)
    with open("task2_decryption_key.json", "w", encoding="utf-8") as file:
        json.dump(decryption_key, file, ensure_ascii=False, indent=4)

def main() -> None:
    parser = argparse.ArgumentParser(description='Processing images from a CSV file.')
    parser.add_argument('enc_text', type=str, help='Path to the enc text.')
    args = parser.parse_args()

    encrypted_text = read_file(args.enc_text)
    decryption_key = comp_key(encrypted_text)
    decrypted_text = decrypt_text(encrypted_text, decryption_key)
    try:
        write_to_file(decrypted_text, decryption_key)
        print("Дешифрование завершено!")
        print("Результаты сохранены в файлы: task2_decrypted_text.txt и task2_decryption_key.json")
    except Exception as e:
        print("Произошла ошибка при сохранении/записи текста:", str(e))

if __name__ == "__main__":
    main()