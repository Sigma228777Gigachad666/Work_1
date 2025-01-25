x = int(input())
y = int(input())
z = int(input())

if x == y == z:
    print("Равностороний")
elif x == y and z != y:
    print("Равнобедренный")
elif x != y and y != z:
    print("Разностороний")