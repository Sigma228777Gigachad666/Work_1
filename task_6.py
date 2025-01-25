x = int(input())
y = int(input())
z = str(input())

if z == '+':
    print(x + y)
elif z == '/':
    print(x / y)
elif z == '/' and y == 0:
    print('На ноль делить нельзя')
elif z == '+':
    print(x + y)
elif z == '-':
    print(x - y)