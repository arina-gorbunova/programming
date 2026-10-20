#Задание 1
import math

print(f"{'x':>8} {'sin(x)':>10}")
print("-" * 20)

for i in range(11):
    x = i * math.pi / 10
    y = math.sin(x)
    print(f"{x:8.4f} {y:10.4f}")

#для y = cos(x)
print(f"{'x':>8} {'cos(x)':>10}")
print("-" * 20)

for i in range(11):
    x = i * math.pi / 10
    y = math.cos(x)
    print(f"{x:8.4f} {y:10.4f}")

#для y = tg(x)
print(f"{'x':>8} {'tan(x)':>10}")
print("-" * 20)

for i in range(11):
    x = i * math.pi / 10
    if i == 5: # проверяем, тк в точке x = пи/2 тангенс не существует
        print(f"{x:8.4f} {'не существует':>10}")
    else:
        y = math.tan(x)
        print(f"{x:8.4f} {y:10.4f}")
    


