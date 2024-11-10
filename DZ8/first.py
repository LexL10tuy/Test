num1 = int(input('Введите первое число: '))
num2 = int(input('Укажите второе число: '))

user_list = [i for i in range(num1, num2 + 1)]
odd = [i for i in user_list if i % 2 != 0 and i != 0] #четные
print(odd)
even = [i for i in user_list if i % 2 == 0] #нечетные
print(even)
for_nine = [i for i in user_list if i % 9 == 0] #кратные 9ти
print(for_nine)
print('Среднее арифмитическое нечетных', sum(odd) / len(odd))
print('Среднее арифмитическое четных', sum(even) / len(even))
print('Среднее арифмитическое кратных девяти', sum(for_nine) / len(for_nine))