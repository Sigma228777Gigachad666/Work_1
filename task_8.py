x = int(input())

if x == 0:
    print('зелёный')
elif x == 2 or 4 or 6 or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 29 or 31 or 33:
    print("чёрный")
elif x > 36:
    print('ошибка ввода')
else:
    print('красный')