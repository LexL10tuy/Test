number = int(input('Введите число: '))
degree = int(input('Введите степень числа: '))
if degree >= 0 and degree <= 7:
    print(number ** degree)
else:
    print('Не буду считать')