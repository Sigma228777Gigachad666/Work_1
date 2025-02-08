x = float(input())
x_str = str(x)
parts =x_str.split('.')
if len(parts)> 1:
    decimal_part = parts[1]
    if decimal_part:
        fist_digit_after_decimal = decimal_part[0]
        print(fist_digit_after_decimal)
    else:
        print("Нет цифр после десятичной точки")
else:
    print("Нет цифр после десятичной точки")
