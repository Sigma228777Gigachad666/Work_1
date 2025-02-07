x = int(input())
y = int(input())
z = int(input())

if x > y and x > z and y < z:
    print(x, z, y)
elif x > y and x > z and z < y:
    print(x, y, z)
elif y > x and y > z and x < z:
    print(y, z, x)
elif y > x and y > z and z < x:
    print(y, x, z)
elif z > x and z > y and x < y:
    print(z, y, x)
elif z > x and z > y and y < x:
    print(z, x, y)