import math

x=float(input("введите x : "))
y=float(input("введите y : "))

if x > 4 and 4<y < 14 :
    f =6 * y - x**2
elif x < 3 or y < 2 :
    f = 5 * x * y
else :
    f = math.atan(x)

print ("Значение функции f : ",f )