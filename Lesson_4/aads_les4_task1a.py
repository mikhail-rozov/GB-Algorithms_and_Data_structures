# Измерить время работы кода при помощи timeit и cProfile.
# Результаты измерений сохранить в файл с кодом в виде комментариев.
# При необходимости, изменить исходный код.

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
import cProfile


# Функция без использования методов max и min:
def find_max(n):

    matrix = [[randint(0, round(1.5 * n)) for _ in range(n)] for _ in range(n)]
    cols_min = [line[0] for line in matrix]

    # for line in matrix:
    #     for number in line:
    #         print(f'{number:>5}', end='')
    #     print()

    for line in matrix:
        for i, number in enumerate(line):
            if number < cols_min[i]:
                cols_min[i] = number

    max_cols_min = cols_min[0]

    for number in cols_min:
        if number > max_cols_min:
            max_cols_min = number

    return max_cols_min


# Функция, написанная с помощью методов max и min:
def find_max_2(n):

    matrix = [[randint(0, round(1.5 * n)) for _ in range(n)] for _ in range(n)]

    # for line in matrix:
    #     for number in line:
    #         print(f'{number:>5}', end='')
    #     print()

    return max([min(line) for line in list(zip(*matrix))])

# print(find_max(5))
# print(find_max_2(5))

# Время работы функции 1 (из урока № 3):                    Время работы функции 2 (с использованием методов min и max):
# ----------------------------------------                  ------------------------------------------------------------

# "aads_les4_task1a.find_max(10)"                           "aads_les4_task1a.find_max_2(10)"
# 1000 loops, best of 5: 69.5 usec per loop                 1000 loops, best of 5: 67.8 usec per loop

# "aads_les4_task1a.find_max(20)"                           "aads_les4_task1a.find_max_2(20)"
# 1000 loops, best of 5: 243 usec per loop                  1000 loops, best of 5: 232 usec per loop

# "aads_les4_task1a.find_max(30)"                           "aads_les4_task1a.find_max_2(30)"
# 1000 loops, best of 5: 550 usec per loop                  1000 loops, best of 5: 538 usec per loop

# "aads_les4_task1a.find_max(100)"                          "aads_les4_task1a.find_max_2(100)"
# 1000 loops, best of 5: 6.16 msec per loop                 1000 loops, best of 5: 5.93 msec per loop


# cProfile.run('find_max(10)')                              cProfile.run("find_max_2(10)")
# 689 function calls in 0.000 seconds                       721 function calls in 0.000 seconds

# cProfile.run('find_max(20)')                              cProfile.run("find_max_2(20)")
# 2414 function calls in 0.001 seconds                      2435 function calls in 0.001 seconds

# cProfile.run('find_max(100)')                             cProfile.run("find_max_2(100)")
# 67116 function calls in 0.014 seconds                     67105 function calls in 0.014 seconds


# Вывод: оба алгоритма имеют квадратичную сложность, обусловленную генерацией квадратной матрицы и операциями с
# каждым ее элементом. Использование функций min и max не позволило значительно снизить сложность алгоритма,
# но позволило написать функцию в 2 строки.
