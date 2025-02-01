x = str(input())
y = str(input())

if x == 'красный' and y == 'синий' or  x == 'синий' and y == 'красный':
    print('фиолетовый')
elif x == 'красный' and y == 'красный':
    print('красный')
elif x == 'синий' and y == 'синий':
    print('синий')
elif x == 'желтый' and y == 'желтый':
    print('желтый')
elif x == 'красный' and y == 'желтый' or  x ==  'желтый' and y == 'красный':
    print('оранжевый')
elif x == 'синий' and y == 'желтый' or  x == 'желтый' and y == 'синий':
    print('зелёный')
elif x != 'красный' and x != 'синий' and x != 'желтый' or y != 'желтый' and y != 'синий' and y != 'красный':
    print('ошибка цвета')