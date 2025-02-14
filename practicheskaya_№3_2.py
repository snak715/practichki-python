user_input = input("Введите один символ: ")

if len(user_input) == 1:
    char = user_input[0]
    if char.isalpha():
        print(f"Буква: {char}")
    elif char.isdigit():
        print(f"Цифра: {char}")
    else:
        print("а")
else:
    print("Пожалуйста, введите только один символ.")