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



# # Задание 3
# def caesar_cipher(text: str, shift: int) -> str:
#     """Шифрует текст шифром Цезаря."""
#     result = []
#     for char in text:
#         if char.isalpha():
#             base = ord('A') if char.isupper() else ord('a')
#             shifted = (ord(char) - base + shift) % 26 + base
#             result.append(chr(shifted))
#         else:
#             result.append(char)
#     return "".join(result)

# # Шифрование
# original = "Hi! My name is Arina"
# encrypted = caesar_cipher(original, 3)
# print(f"Оригинал: {original}")
# print(f"Зашифровано: {encrypted}")  # Kl! Pb qdph lv Dulqd

# # Дешифрование (сдвиг в обратную сторону)
# decrypted = caesar_cipher(encrypted, -3)
# print(f"Расшифровано: {decrypted}")  # Hi! My name is Arina



# # Задание 4
# import re

# def validate_email(email: str) -> bool:
#     """Проверяет корректность email."""
#     pattern = r'^[\w.+-]+@[\w-]+\.[\w.-]+$'
#     return bool(re.match(pattern, email))

# def validate_phone(phone: str) -> bool:
#     """Проверяет корректность российского телефона."""
#     pattern = r'^\+7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
#     return bool(re.match(pattern, phone))

# def validate_url(url: str) -> bool:
#     """Проверяет корректность URL."""
#     pattern = r'^https://[\w.-]+\.[a-z]{2,}(/[\w./-]*)?$'
#     return bool(re.match(pattern, url))

# # Тесты
# tests = [
#     ("email", "ivan@example.com", validate_email),
#     ("email", "invalid@", validate_email),
#     ("phone", "+7 (999) 123-45-67", validate_phone),
#     ("url", "https://example.com", validate_url),
#     ("url", "not-a-url", validate_url),
# ]

# for type_, value, validator in tests:
#     result = "✓" if validator(value) else "✗"
#     print(f"{result} {type_}: {value}")


# # Задание 5
# students = [
#     ("Иван", 25, 4.5),
#     ("Мария", 22, 4.85),
#     ("Пётр", 30, 4.2),
#     ("Анна", 20, 4.95),
# ]

# # Заголовок
# print(f"{'Имя':<10} {'Возраст':>8} {'Балл':>8}")
# print("-" * 28)

# # Данные
# for name, age, gpa in students:
#     print(f"{name:<10} {age:>8} {gpa:>8.2f}")

# # Итого
# print("-" * 28)
# avg_gpa = sum(s[2] for s in students) / len(students)
# print(f"{'Средний балл':<10} {'':>8} {avg_gpa:>8.2f}")


# Задание 6 (в группе)
# Подсчет частоты каждой буквы (в исходном тексте или своем)
from collections import Counter

def count_letters(text):
    # Оставляем только буквы и приводим к нижнему регистру
    letters = [char.lower() for char in text if char.isalpha()]
    return Counter(letters)

# Готовый текст для второго варианта
default_text = "Привет, мир! Hello World. Это тестовый текст для проверки частоты букв"

print("1. Ввести свой текст")
print("2. Использовать готовый текст")

while True:
    try:
        choice = int(input("Введите номер варианта (1 или 2): "))
        if choice in (1, 2):
            break
        else:
            print("Вы выбрали не 1 и не 2. Попробуйте снова")
    except ValueError:
        print("Ошибка! Вы ввели не цифру")

if choice == 1:
    text = input("Введите ваш текст: ")
else: 
    text = default_text
    print(f"Используется готовый текст:\n{text}")


# Подсчет и вывод
result = count_letters(text)

result = count_letters(text)
# Проверка, что в тексте есть буквы
if not result:
    print("\nВ тексте нет букв — подсчитывать нечего.")
else:
    print("\nЧастота букв:")
    for letter, count in sorted(result.items()):
        print(f"'{letter}': {count}")