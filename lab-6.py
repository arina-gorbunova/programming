# #Задание 1
# import random 

# n = int(input("Введите N: "))

# numbers = [random.randint(1, 100) for _ in range(n)] #создаем список длины n 

# print(f"Исходный список: {numbers}")
# print(f"Сумма: {sum(numbers)}")
# print(f"Среднее: {sum(numbers)/len(numbers):.2f}")
# print(f"Минимум: {min(numbers)}")
# print(f"Максимум: {max(numbers)}")

# #сортируем
# numbers.sort()
# print(f"Отсортированный: {numbers}")

# #без дубликатов
# unique = list(dict.fromkeys(numbers))
# print(f"Без дубликатов: {unique}")


#Задание 2
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

#через словарь с подсчётом
from collections import Counter
counts = Counter(numbers)
duplicates = [num for num, count in counts.items() if count > 1]

print(f"Дубликаты(через словарь): {duplicates}")  #[1, 2, 3]

#через множества
seen = set()
duplicates2 = set()
for num in numbers:
    if num in seen:
        duplicates2.add(num)
    seen.add(num)

print(f"Дубликаты(через множества): {list(duplicates2)}")
