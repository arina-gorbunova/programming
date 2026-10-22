# #Задание 1
# import math

# print(f"{'x':>8} {'sin(x)':>10}")
# print("-" * 20)

# for i in range(11):
#     x = i * math.pi / 10
#     y = math.sin(x)
#     print(f"{x:8.4f} {y:10.4f}")

# #для y = cos(x)
# print(f"{'x':>8} {'cos(x)':>10}")
# print("-" * 20)

# for i in range(11):
#     x = i * math.pi / 10
#     y = math.cos(x)
#     print(f"{x:8.4f} {y:10.4f}")

# #для y = tg(x)
# print(f"{'x':>8} {'tan(x)':>10}")
# print("-" * 20)

# for i in range(11):
#     x = i * math.pi / 10
#     if i == 5: # проверяем, тк в точке x = пи/2 тангенс не существует
#         print(f"{x:8.4f} {'не существует':>10}")
#     else:
#         y = math.tan(x)
#         print(f"{x:8.4f} {y:10.4f}")


# #Задание 2
# n = int(input("Введите N: "))

# sum_numbers = 0
# product = 1
# sum_squares = 0

# for i in range(1, n + 1):
#     sum_numbers += i
#     product *= i
#     sum_squares += i ** 2

# print(f"Сумма: {sum_numbers}")
# print(f"Произведение (N!): {product}")
# print(f"Сумма квадратов: {sum_squares}")


# #Задание 3
# n = int(input("Введите N: "))

# a, b = 0, 1

# print(f"Первые {n} чисел Фибоначчи:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# print()

# #через рекурсию
# def fib(n):
#     if n <= 1: 
#         return n 
#     return (fib(n - 1) + fib(n - 2))

# print(f"Первые {n} чисел Фибоначчи(через рекурсию):")
# for i in range(n):
#     print(fib(i), end=" ")



# #Задание 4
# n = int(input("Введите число: "))
# original = n
# factors = []

# divisor = 2
# while divisor * divisor <= n:
#     while n % divisor == 0:
#         factors.append(divisor)
#         n //= divisor
#     divisor += 1
# if n > 1:
#     factors.append(n)

# print(f"{original} = {' x '.join(map(str, factors))}")



#Задание 5
n = int(input("Введите число: "))
original = n

count = 0
total = 0
product = 1
reversed_num = 0

while n > 0:
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    reversed_num = reversed_num * 10 + digit 
    n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {product}")
print(f"Перевернутое число: {reversed_num}")