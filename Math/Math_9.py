x = input()

print('Цифра в позиции тысяч равна' ,int(x) // 1000)
print('Цифра в позиции сотен равна' ,int(x) % 1000 // 100)
print('Цифра в позиции десятков равна' ,int(x) % 100 // 10)
print('Цифра в позиции единиц равна' ,int(x) % 10) 
#Complete