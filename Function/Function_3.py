x = input()

if (int(x) // 1000) + (int(x) % 10) == (int(x) % 1000 // 100) - (int(x) % 100 // 10):
    print('ДА')
else:
    print('НЕТ')