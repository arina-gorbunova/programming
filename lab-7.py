# # Задание 1
# def count_words(text: str) -> int:
#     """Подсчитывает количество слов в тексте."""
#     return len(text.split())

# text = input("Введите текст: ")
# print(f"Количество слов: {count_words(text)}")

# import re
# def count_words_clean(text: str) -> int:
#     """Подсчитывает слова, игнорируя пунктуацию."""
#     words = re.findall(r'\b\w+\b', text)
#     return len(words)

# text = "Привет, мир! Как дела?"
# print(f"Слов (с пунктуацией): {count_words(text)}")
# print(f"Слов (без пунктуации): {count_words_clean(text)}")


# # Задание 2
# import re

# def is_palindrome(text: str) -> bool:
#     "Проверяет является ли строка палиндромом."
#     # Очистка: только буквы и цифры, нижний регистр
#     cleaned = re.sub(r'[^\w]', '', text.lower())
#     return cleaned == cleaned[::-1]

# # Тесты
# tests = [
#     "Hello World!",
#     "1654561",
#     "programming",
#     "racecar",
#     "палиндром или нет?",
#     "Hi! My name is Arina"
# ]

# for text in tests:
#     result = "палиндром" if is_palindrome(text) else "не палиндром"
#     print(f"'{text}' - {result}")



# Задание 3
def caesar_cipher(text: str, shift: int) -> str:
    """Шифрует текст шифром Цезаря."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

# Шифрование
original = "Hi! My name is Arina"
encrypted = caesar_cipher(original, 3)
print(f"Оригинал: {original}")
print(f"Зашифровано: {encrypted}")  # Kl! Pb qdph lv Dulqd

# Дешифрование (сдвиг в обратную сторону)
decrypted = caesar_cipher(encrypted, -3)
print(f"Расшифровано: {decrypted}")  # Hi! My name is Arina
