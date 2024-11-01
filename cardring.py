print('Открой машину')
answer = int(input('Введите 1, если у Вас автомат, и 2, если у Вас механика'))
if answer == 1:
    print('Выжимаем тормоз')
elif answer == 2:
    print('Выжимаем сцепление')
print('Поверни ключ')
if answer == 1:
    print('Включи Drive. Отпускай тормоз')
elif answer == 2:
    print('Включи первую. Отпускай сцепление')
print('ты едешь')
