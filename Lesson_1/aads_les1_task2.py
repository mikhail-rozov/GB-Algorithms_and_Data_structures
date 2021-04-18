# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.

point = input('Введите координаты x, y первой точки через запятую: ')
x_1 = int(point.replace(' ', '').split(',')[0])
y_1 = int(point.replace(' ', '').split(',')[1])

point = input('Введите координаты x, y второй точки через запятую: ')
x_2 = int(point.replace(' ', '').split(',')[0])
y_2 = int(point.replace(' ', '').split(',')[1])

k = (y_1 - y_2) / (x_1 - x_2)
b = y_1 - k * x_1

if k == 0:
    print(f'y = {b}')
elif b > 0:
    print(f'y = {k}x + {b}')
elif b == 0:
    print(f'y = {k}x')
else:
    print(f'y = {k}x - {abs(b)}')
