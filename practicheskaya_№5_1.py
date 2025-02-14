n = int(input('Введите число n до 99 : '))
k = int(input('Введите число k :  '))
if n < 99:
    new = []
    new.extend([k, n, k])
    print (new)
else:
    print("Число n должно быть меньше 99 ")