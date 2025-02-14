n = int(input('введите n : '))
a = int(input('Введите a : '))
result = []
for i in range (2, n + 1 ):
    o_sum = sum(int(d) for d in str(i))
    new_sum = sum(int(d) for d in str(o_sum * a))
    if o_sum == new_sum :
        result.append(i)
print (result)
