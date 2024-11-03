# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# num3 = int(input('Введите число 3: '))
numbers = [int(i) for i in input('Введите три числа: ') if i.isdigit()]
sign = input('Введите знак: ')
if sign == '*':
    proisvedenie = 1
    for i in numbers:
    proisvedenie *= int(simbol)
    print(proisvedenie)
elif sign == '+':
    sum = 0
    for simbol in numbers:
    sum += int(simbol)
    print(sum)