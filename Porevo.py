def absolute_sum():
    total = 0 
    for _ in range(5):
        num=float(input())
        total += abs(num)
    print(total)

absolute_sum()