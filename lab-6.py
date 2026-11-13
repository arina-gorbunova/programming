#Задание 1
import random 

n = int(input("Введите N: "))

numbers = [random.randint(1, 100) for _ in range(n)] #создаем список длины n 

print(f"Исходный список: {numbers}")
print(f"Сумма: {sum(numbers)}")
print(f"Среднее: {sum(numbers)/len(numbers):.2f}")
print(f"Минимум: {min(numbers)}")
print(f"Максимум: {max(numbers)}")

#сортируем
numbers.sort()
print(f"Отсортированный: {numbers}")

#без дубликатов
unique = list(dict.fromkeys(numbers))
print(f"Без дубликатов: {unique}")
