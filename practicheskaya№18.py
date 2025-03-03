import sympy as sp

x = sp.symbols('x')
f = sp.exp(x**2 / 2)

n = int(input("Введите порядок производной n: "))
f_n = sp.diff(f, x, n)
print(f"{n}-я производная функции f(x): {f_n}")
