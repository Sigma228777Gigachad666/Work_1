n = int(input("Введите количество собачьих лет: "))

if n <= 0:
    print("Количество собачьих лет должно быть натуральным числом.")
elif n == 1:
    human_years = 10.5
elif n == 2:
    human_years = 21.0
else:
    human_years = 21.0 + (n - 2) * 4

print(human_years)