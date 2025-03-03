numbers = []  
while True:
    try:
        num = int(input("Введите число : "))

        numbers.append(num) 

    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное число.")  

if not numbers:
    print("Список пуст. Не удалось найти максимальное значение.")
    return None

max_value = max(numbers)
print(f"Максимальное значение в списке: {max_value}")

