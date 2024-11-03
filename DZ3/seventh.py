metres = int(input('Введите метры: '))
sm = metres * 100
dm = metres * 10
ml = round(metres / 1600, 2)
print(metres, sm, dm, ml)