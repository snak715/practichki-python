import math

        x = float(input("Введите значение x: "))
        y = float(input("Введите значение y: "))

perv = x - 10 * math.sin(x) + abs(x**4 - x**5)

if math.cos(x) - math.sin(y) == 0:
    print("Второе выражение не может быть вычислено (деление на ноль).")
else:
    vtor = (math.sin(x) + math.cos(y)) / (math.cos(x) - math.sin(y)) * math.tan(x * y)

# Вывод результатов
print(f"Первое выражение: {perv}")
print(f"Второе выражение: {vtor}")
