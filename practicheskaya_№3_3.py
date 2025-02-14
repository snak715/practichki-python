x = float(input("Введите значение x: "))

if x > 3:
    result = 2 * x**2 - 3 * x - 9
else:
    result = 12.1 / (2 * x**2 + 1)

print(f"Значение функции F(x) при x = {x} равно {result}")