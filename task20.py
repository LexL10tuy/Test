num = input("Введите четырехзначное число: ")
print(f"{num[3] + num[2] + num[1] + num[0]}")

print(f"{int(num[2] + num[3] + num[0] + num[1])}")
num_pro1 = int(num) // 100
num_pro2 = int(num) % 100
print(f'{str(num_pro2) + str(num_pro1)}')