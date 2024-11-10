number = 0

while number != 7:
    number = int(input('Введите число: '))
    if number > 0 and number != 7:
        print('Is positive')
    elif number < 0:
        print('Is negative')
    elif number == 7:
        print('Bye')
        break
    else:
        print('Eguel zero')