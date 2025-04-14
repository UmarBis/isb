
def encrypt(text: str, key: str) -> str:
    """
    Шифрует текст с помощью ключа
    :param text: исходный текст
    :param key: ключ
    :return: зашифрованный ключ
    """
    return ''.join(key.get(char, char) for char in text.lower())

def invert_key(key):
    """Создаёт обратный ключ для дешифрования."""
    return {v: k for k, v in key.items()}
def decrypt(text, key):
    """Расшифровывает текст, используя обратный ключ."""
    inverted_key = invert_key(key)
    return ''.join(inverted_key.get(char, char) for char in text.lower())


