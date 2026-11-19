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


# #Задание 2
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

# #через словарь с подсчётом
# from collections import Counter
# counts = Counter(numbers)
# duplicates = [num for num, count in counts.items() if count > 1]

# print(f"Дубликаты(через словарь): {duplicates}")  #[1, 2, 3]

# #через множества
# seen = set()
# duplicates2 = set()
# for num in numbers:
#     if num in seen:
#         duplicates2.add(num)
#     seen.add(num)

# print(f"Дубликаты(через множества): {list(duplicates2)}")



# #задание 3
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Через zip
# transposed = [list(row) for row in zip(*matrix)]

# # Вывод
# print("Исходная матрица:")
# for row in matrix:
#     print(row)

# print("\nТранспонированная матрица:")
# for row in transposed:
#     print(row)


# #задание 4
# students = [
#     ("Иван", 25, 4.5),
#     ("Мария", 22, 4.8),
#     ("Петр", 30, 4.2),
#     ("Анна", 20, 4.9)
# ]

# #Самый старший
# oldest = max(students, key=lambda s: s[1])
# print(f"Самый старший: {oldest[0]}, {oldest[1]} лет")

# #С самым высоким баллом
# best = max(students, key=lambda s: s[2])
# print(f"Лучший студент: {best[0]}, балл {best[2]}")

# #Средний возраст
# avg_age = sum(s[1] for s in students) / len(students)
# print(f"Средний возраст: {avg_age:.1f}")

# #Сортировка по баллу (убывание)
# sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
# print("\nПо баллу:")
# for name, age, gpa in sorted_students:
#     print(f"{name}: {gpa}")


#задание 5

#через множества
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Объединение: {sorted(union)}")
print(f"Пересечение: {sorted(intersection)}")
print(f"Разность: {sorted(difference)}")

#с сохранением порядка
union_ordered = list1 + [x for x in list2 if x not in list1]
intersection_ordered = [x for x in list1 if x in list2]

print(f"Объединение(через генератор списков): {union_ordered}")
print(f"Пересечение(через генератор списков): {intersection_ordered}")
