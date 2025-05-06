n = int(input())
counter = 0
while n > 1:
    n %= 10
    if n % 2 == 0:
        counter += n
print(counter)