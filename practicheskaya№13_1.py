import random

with open('numbers.txt', 'w') as file:
    for _ in range(100):  
        file.write(f"{random.randint(1, 100)}\n")

count = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        num = int(line.strip())
        if num % 2 != 0 and (num * 2) in range(1, 201):  
            count += 1

print(f"Количество удвоенных нечетных чисел: {count}")