from collections import Counter

def comp_key(encrypted_text: str, rus_frq: str):
    """
    Высчитывание частот символов нашего текста и составление ключа путем сопоставления частот алфавита
    :param encrypted_text: зашифрованный текст
    :param rus_frq: частоты русского алфавита
    :return: ключ для дешифра
    """
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



