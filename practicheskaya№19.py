class Stack:
    def __init__(self):
        self.stack = [0] * 1024
        self.top = 0

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == 1024

    def push(self, value):
        if self.is_full():
            print("Ошибка: стек переполнен")
            return
        self.stack[self.top] = value
        self.top += 1

    def pop(self):
        if self.is_empty():
            print("Ошибка: стек пуст")
            return None
        self.top -= 1
        return self.stack[self.top]

    def top_equals(self, k):
        return not self.is_empty() and self.stack[self.top - 1] == k


def evaluate_rpn_file(filename):
    try:
        with open(filename, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            results = []

            for line in lines:
                stack = Stack()
                tokens = line.strip().split()

                for token in tokens:
                    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                        stack.push(int(token))
                    else:
                        b, a = stack.pop(), stack.pop()
                        if a is None or b is None:
                            print("Ошибка: некорректное выражение")
                            return
                        try:
                            if token == '+':
                                stack.push(a + b)
                            elif token == '-':
                                stack.push(a - b)
                            elif token == '*':
                                stack.push(a * b)
                            elif token == '/':
                                stack.push(a // b)
                            else:
                                print(f"Ошибка: неизвестный оператор {token}")
                                return
                        except ZeroDivisionError:
                            print("Ошибка: деление на ноль")
                            return

                result = stack.pop()
                if result is not None:
                    results.append(str(result))

            file.write('\n' + '\n'.join(results) + '\n')
            print("Результаты дописаны в файл.")

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    except Exception as e:
        print(f"Ошибка: {e}")


def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(ord(char))

    reversed_string = ''.join(chr(stack.pop()) for _ in range(len(s)))
    return reversed_string


if name == "__main__":
    while True:
        try:
            print("\nВыберите действие:")
            print("1. Вычислить выражения в обратной польской записи из файла")
            print("2. Перевернуть строку")
            print("3. Выйти")

            choice = input("Введите номер операции: ")
            if choice == "1":
                filename = input("Введите имя файла: ")
                evaluate_rpn_file(filename)
            elif choice == "2":
                s = input("Введите строку: ")
                print("Перевернутая строка:", reverse_string(s))
            elif choice == "3":
                print("Выход.")
                break
            else:
                print("Ошибка: неверный выбор. Попробуйте снова.")

        except Exception as e:
            print(f"Ошибка: {e}")