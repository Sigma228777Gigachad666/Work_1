x = input()
found_digit = False
for i in range(len(x)):     
    if x[i] in "0123456789": # String 
        found_digit = True
        break
if found_digit:     
    print("Цифра")
else:
    print("Цифр нет")
#  -- КАЛ  \\ КУЛ