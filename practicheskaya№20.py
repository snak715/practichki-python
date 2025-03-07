20
def input_number(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")


def task_1():
    x = input_number("Введите значение x: ")
    result = x**2 + 2*x + 1  # Пример расчёта
    print(f"Результат: {result}")


def task_2():
    x = input_number("Введите значение x: ")
    y = input_number("Введите значение y: ")
    result = x * y  # Пример расчёта
    print(f"Результат: {result}")


def task_3():
    s = input("Введите строку: ")
    reversed_s = s[::-1]
    print(f"Перевернутая строка: {reversed_s}")


def task_4():
    numbers = []
    while True:
        num = input("Введите число (или 'stop' для завершения): ")
        if num.lower() == "stop":
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Ошибка: введите корректное число.")
    
    if numbers:
        print(f"Максимальное число: {max(numbers)}")
    else:
        print("Список пуст.")


def task_5():
    n = int(input_number("Введите количество элементов: "))
    numbers = [input_number(f"Введите число {i+1}: ") for i in range(n)]
    print(f"Сумма чисел: {sum(numbers)}")


def main():
    while True:
        try:
            print("\nВыберите задачу:")
            print("1. Решение первой задачи")
            print("2. Решение второй задачи")
            print("3. Переворот строки")
            print("4. Поиск максимального числа")
            print("5. Сумма чисел")
            print("6. Выход")

            choice = input("Введите номер задачи: ")

            if choice == "1":
                task_1()
            elif choice == "2":
                task_2()
            elif choice == "3":
                task_3()
            elif choice == "4":
                task_4()
            elif choice == "5":
                task_5()
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Ошибка: неверный ввод. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")


if name == "__main__":
    main()