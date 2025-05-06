n = input()
a = 0
b = 0
c = 0
d = 0
e = 0
last_digit = int(n) % 10
print('последняя цифра',str(n).count(str(last_digit)))
for i in range(len(str(n))):
    if int(str(n)[i]) == 3:
        a += 1
    if int(str(n)[i]) % 2 == 0:
        b += 1
    if int(str(n)[i]) > 5:
        c += int(n[i])
    if int(str(n)[i]) > 7:
        d *= int(str(n)[i])
    if int(str(n)[i]) == 0 or int(str(n)[i]) == 5:
        e += 1
print('колво 3: ',a)
print('колво четных: ',b)
print('сумма цифр больше 5: ',c)
print('произвед цифр больше 7: ',d)
print('колво 0 и 5: ',e)