numbers = sorted([int(input()) for _ in range(3)], reverse=True)
print(*numbers, sep='\n')