while True:

    try:

        a = list(map(int,input("введите последовательность из 4 чисел a через пробел : ").split()))
        b = list(map(int,input("введите последовательность из 4 чисел b через пробел : ").split()))


        if len(a)!=len(b):
            print('Последовательности не одиноковой длинны!!!')

        for i in range(len(a)):
            if a[i] <=0:
                b[i] *= 10
            else:
                b[i] = 0
        print("Результат b : ", b)
        break
    except:
        print("oшибка")