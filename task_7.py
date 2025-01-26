x = str(input())
y = str(input())

if x == 'красный' and y == 'синий':
    print('фиолетывый')
elif x == 'красный' and y == 'желтый':
    print('оранжевый')
elif x == 'синий' and y == 'желтый':
    print('зелёный')
elif x != 'красный' and x != 'синий' or y != 'желтый' and y != 'синий':
    print('ошибка цвета')