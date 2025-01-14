x = input()

if int(x) < 13:
    print('детство')

if int(x) < 24 and int(x) >= 14:
    print('молодость')

if int(x) < 59 and int(x) >= 25:
    print('зрелость')

if int(x) > 60:
    print('Старость')