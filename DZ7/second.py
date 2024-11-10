num1 = int(input('Укажите начало диапозона: '))
num2 = int(input('Укажите конец диапозона: '))
#for i in range(num1, num2):
    #print(i)
user_list = [i for i in range(num1, num2 + 1)]
print(*user_list[::-1])
print(*[i for i in user_list if i % 7 == 0])
# Количество кратных 5
print(len([i for i in user_list if i % 5 == 0]))