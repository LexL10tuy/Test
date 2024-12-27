num = input("Введите четырехзначное число: ")
print(f"{num[3] + num[2] + num[1] + num[0]}")

print(f"{int(num[2] + num[3] + num[0] + num[1])}")
num_pro1 = str(int(num) // 100)
num_pro2 = str(int(num) % 100)
print(num_pro2 + num_pro1)
