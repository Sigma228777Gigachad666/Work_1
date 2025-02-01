x = int(input())
y = int(input())
z = int(input())

if x > y and x < z or x < y and x > z:
    print(x)
elif y > x and y < z or y < x and y > z:
    print(y)
elif z > x and z < y or z < x and z > y:
    print(z)  