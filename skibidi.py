n = input()
count = 0
for i in range(len(str(n))):
    if int(str(n)[i]) > 5:
        count += int(n[i])
print(count)