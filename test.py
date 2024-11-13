class CaesarsCipher:
    """Класс для шифрования и расшифрования сообщений с помощью шифра Цезаря."""

    def __init__(self):
        self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

    def decrypt(self, message: str, key: int) -> str:
        """Метод для расшифровки сообщения с заданным ключом."""
        decrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) - key) % len(self.characters)
                decrypted_message += self.characters[index]
            else:
                decrypted_message += char  # Оставляем символ без изменений
        return decrypted_message

    def encrypt(self, message: str, key: int) -> str:
        """Метод для шифрования сообщения с заданным ключом."""
        encrypted_message = ""
        for char in message:
            if char in self.characters:
                index = (self.characters.index(char) + key) % len(self.characters)
                encrypted_message += self.characters[index]
            else:
                encrypted_message += char  # Оставляем символ без изменений
        return encrypted_message


def find_key(encrypted_message: str) -> int:
    """Функция для подбора ключа для расшифровки."""
    cipher = CaesarsCipher()
    for key in range(len(cipher.characters)):
        decrypted_message = cipher.decrypt(encrypted_message, key)
        # Проверяем, содержит ли расшифрованное сообщение хотя бы одно слово из списка известных слов
        if "пароль" in decrypted_message:  # Например, если мы знаем, что пароль содержит это слово
            return key, decrypted_message
    return None, None


if __name__ == "__main__":
    encrypted_note = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"
    key, result = find_key(encrypted_note)

    if key is not None:
        print(f'Подобранный ключ: {key}')
        print(f'Расшифрованное сообщение: {result}')
    else:
        print("Ключ не найден.")
