x = int(input())

a = x // 100
b = x % 100 // 10
c = x % 10

if max(a, c) - min(a, c) == b:
    print("Число интересное")
else:
    print('Число неинтересное')