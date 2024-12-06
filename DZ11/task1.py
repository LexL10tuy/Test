# vvod = int(input('Введите сторону квадрата: '))
# for i in range(vvod):
#     for j in range(vvod):

#         print(' * ', end='')
#     print('\n')

# print(" " * 4)


def draw_triangle(fill, base=10):
    n = 10
    for i in range(base):
        i = [fill] * n
        print('(n-1)*' ''.join(i))
        n -= 1


draw_triangle('*')