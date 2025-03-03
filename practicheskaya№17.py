import math

while True:
    try:
        n = int(input("Введите размер матрицы n: "))
        if n <= 0:
            raise ValueError('Размерность должна быть положительным числом')
        break  
    except ValueError as e:
        print(f'Ошибка: {e}. Попробуйте снова')

G = [[3 * math.cos(math.sqrt(i - 2 * j)) for j in range(n)] for i in range(n)]

for row in G:
    print(row)

maxcol = max(row[0] for row in G)
print(f"Максимальный элемент первого столбца: {maxcol}")

row_product = math.prod(G[3])
print(f"Произведение элементов четвертой строки: {row_product}")

min_positive = min(min(filter(lambda x: x > 0, row)) for row in G)
print(f"Минимальный положительный элемент матрицы: {min_positive}")
