# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание: попытайтесь решить задания без использования функций
# max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.

from random import randint

size = 5
matrix = [[randint(0, 10) for _ in range(size)] for _ in range(size)]
cols_min = [line[0] for line in matrix]

for line in matrix:
    for number in line:
        print(f'{number:>5}', end='')
    print()

for line in matrix:
    for i, number in enumerate(line):
        if number < cols_min[i]:
            cols_min[i] = number

max_cols_min = cols_min[0]

for number in cols_min:
    if number > max_cols_min:
        max_cols_min = number

print(f'\nМаксимальный элемент среди минимальных элементов столбцов матрицы - {max_cols_min}')
