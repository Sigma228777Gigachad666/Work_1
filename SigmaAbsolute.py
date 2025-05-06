n = input()
count = 0
for i in range(len(str(n))):
    if int(str(n)[i]) % 2 == 0:
        count += 1
print(count)