x = int(input())
y = int(input())
z = str(input())

if z == '*':
    print(x * y)
elif z == '/':
    if y == 0:
        print('На ноль делить нельзя')
    else:
        result = x / y
        print(result)
elif z == '+':
    print(x + y)
elif z == '-':
    print(x - y)