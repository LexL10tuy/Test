num1 = int(input('Укажите начало диапозона: '))
num2 = int(input('Укажите конец диапозона: '))
for i in range(num1 , num2 + 1):
    if i % 7 == 0:
        print(i)