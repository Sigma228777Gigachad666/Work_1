number = float(input("Введите положительное действительное число"))

first_digit_after_decimal = str(number).split('.')[1][0]
                                    # 3.123151251
print(first_digit_after_decimal)