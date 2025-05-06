n = input()
count = 1
for i in range(len(str(n))):
    if int(n[i]) > 7:
        count *= int(n[i])
print(count)