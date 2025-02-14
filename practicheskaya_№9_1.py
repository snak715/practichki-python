import math
while True:
    try:

        N=int(input("Введите количество чисел n : "))
        if N <= 1:
            print("Количество чисел должно быть больше 1.")

        numb = []
        for i in range(N):
            num = float(input(f"Введите число {i+1} : "))
            numb.append(num)

        M = sum(numb)/N

        S = [math.sqrt(sum((x-M)**2 for x in numb ) /(N-1)) ]
        print(f"Результаты S : {S} ")

        break

    except:
        print("Некоретный ввод данных")
        