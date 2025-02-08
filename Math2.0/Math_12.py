def is_interesting_number():
    number = input()

    digit1= int(number[0])
    digit2= int(number[1])
    digit3= int(number[2])

    maximum = max(digit1, digit2, digit3)
    minimum = min(digit1, digit2, digit3)
    if digit1 != maximum and digit1 != minimum:
        middle = digit1
    elif digit2 != maximum and digit2 != minimum:
        middle = digit2
    else:
        middle = digit3
    if maximum - minimum == middle:
        print("Число интересное")
    else:
        print("Число неинтересное")
is_interesting_number()
