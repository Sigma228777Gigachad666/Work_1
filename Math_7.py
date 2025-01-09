x = input()

y = (int(x) % 10**3) // 10**2
z = (int(x) % 10**2) // 10**1
w = (int(x) % 10**1) // 10**0

print('Сумма цифр =', y + z + w)
print('Произведение цифр =', y * z * w)
#Complete