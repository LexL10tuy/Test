number = int(input('Введите число от 1 до 100: '))
if number < 1 or number > 100:
    print('Число не из диапазона')
elif number % 3 == 0 and number % 5 == 0: 
    print('Fizz')
elif number % 3 == 0: 
    print('Fizz')
elif number % 5 == 0: 
    print('Buzz')
else:
    print(number)