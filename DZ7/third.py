num1 = int(input('Укажите начало диапозона: '))
num2 = int(input('Укажите конец диапозона: '))
user_list = [i for i in range(num1, num2 + 1)]
for i in user_list:
    if i % 3 == 0 and i % 5 == 0: 
        print('FizzBuzz')
    elif i % 3 == 0: 
        print('Fizz')
    elif i % 5 == 0: 
        print('Buzz')
    else:
        print(i)