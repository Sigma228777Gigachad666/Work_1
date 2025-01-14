x = input()
y = input()
z = input()

if int(x) > int(z) and int(y) > int(z):
    print(int(x) + int(y))

if int(x) == int(z) and int(y) == int(z):
    print(int(x) + int(y) + int(z))


if int(x) > int(y) and int(z) > int(y):
    print(int(x) + int(z))


if int(z) > int(x) and int(y) > int(x):
    print(int(z) + int(y))


if int(x) < 0 and int(y) < 0 and int(z) < 0:
    print('0')