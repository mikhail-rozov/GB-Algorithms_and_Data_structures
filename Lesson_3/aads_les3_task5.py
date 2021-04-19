# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.
# Примечание: попытайтесь решить задания без использования функций max,
# min, sum, sorted и их аналогов, в том числе написанных самостоятельно.
# Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint

numbers = [randint(-10, 10) for _ in range(10)]
max_number = None

print(f'Дан список:\n{numbers}')

for number in numbers:
    if number < 0:
        max_number = number
        break

for number in numbers:
    if number < 0:
        if number > max_number:
            max_number = number

try:
    print(f'\nМаксимальное отрицательное число в списке - ({max_number}), его позиция в списке - '
          f'{numbers.index(max_number)}')
except ValueError:
    print('\nВ списке отсутствуют отрицательные числа')
