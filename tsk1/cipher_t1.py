def encrypt(text: str, key: str) -> str:
    """
    Шифрует текст с помощью ключа
    :param text: исходный текст
    :param key: ключ
    :return: зашифрованный ключ
    """
    return ''.join(key.get(char, char) for char in text.lower())


def invert_key(key: str) -> str:
    """
    Инверсия ключа
    :param key: ключ
    :return: обратный ключ
    """
    return {v: k for k, v in key.items()}


def decrypt(text: str, key: str) -> str:
    """
    Дешифрованный текст
    :param text: зашифрованный текст
    :param key: ключ
    :return:
    """
    inverted_key = invert_key(key)
    return ''.join(inverted_key.get(char, char) for char in text.lower())



