k = int(input('Введите день от 1 до 365: '))
#a 1 января - понедельник
day = k - k//7*7
if day == 0:
    print('Monday')
elif day == 1:
    print('Вторник')
elif day == 2:
    print('Среда')
elif day == 3:
    print('Четверг')
elif day == 4:
    print('Пятница')
elif day == 5:
    print('Суббота')
elif day == 6:
    print('Воскресенье')