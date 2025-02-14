x = float(input("Введите число x: "))
y = float(input("Введите число y: "))
z = float(input("Введите число z: "))


pervay_xyz = x + y + z
vtoraya_xyz = x * y * z

max_sum = max(pervay_xyz, vtoraya_xyz)

# Вывод результата
print(f"Максимум из суммы и произведения: {max_sum}")
