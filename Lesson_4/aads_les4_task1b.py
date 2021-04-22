# Измерить время работы кода при помощи timeit и cProfile.
# Результаты измерений сохранить в файл с кодом в виде комментариев.
# При необходимости, изменить исходный код.

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и
# их аналогов, в том числе написанных самостоятельно.
# Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint
import cProfile


# Функция без использования методов max и min:
def exchange_min_max(n):

    the_list = [randint(-100, 100) for _ in range(n)]

    # print(the_list)

    max_number = min_number = the_list[0]

    for number in the_list:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    spam = the_list.index(min_number)
    the_list[the_list.index(max_number)] = min_number
    the_list[spam] = max_number

    return the_list


# Функция, написанная с помощью методов max и min:
def exchange_min_max_2(n):

    the_list = [randint(-100, 100) for _ in range(n)]

    # print(the_list)

    max_ = max(the_list)
    min_ = min(the_list)

    spam = the_list.index(min_)
    the_list[the_list.index(max_)] = min_
    the_list[spam] = max_

    return the_list


# Время работы функции 1 (из урока № 3):                    Время работы функции 2 (с использованием методов min и max):
# ----------------------------------------                  ------------------------------------------------------------

# "aads_les4_task1b.exchange_min_max(10)"                   "aads_les4_task1b.exchange_min_max_2(10)"
# 1000 loops, best of 5: 5.73 usec per loop                 1000 loops, best of 5: 5.82 usec per loop

# "aads_les4_task1b.exchange_min_max(30)"                   "aads_les4_task1b.exchange_min_max_2(30)"
# 1000 loops, best of 5: 16 usec per loop                   # 1000 loops, best of 5: 16 usec per loop

# "aads_les4_task1b.exchange_min_max(100)"                  "aads_les4_task1b.exchange_min_max_2(100)"
# 1000 loops, best of 5: 50.9 usec per loop                 1000 loops, best of 5: 51 usec per loop

# "aads_les4_task1b.exchange_min_max(500)"                  "aads_les4_task1b.exchange_min_max_2(500)"
# 1000 loops, best of 5: 254 usec per loop                  1000 loops, best of 5: 250 usec per loop


# cProfile.run('exchange_min_max(10)')                      # cProfile.run('exchange_min_max_2(10)')
# 63 function calls in 0.000 seconds                        # 63 function calls in 0.000 seconds

# cProfile.run('exchange_min_max(100)')                     cProfile.run('exchange_min_max_2(100)')
# 535 function calls in 0.000 seconds                       532 function calls in 0.000 seconds

# cProfile.run('exchange_min_max(500)')                     cProfile.run('exchange_min_max_2(500)')
# 2646 function calls in 0.001 seconds                      # 2646 function calls in 0.001 seconds


# Вывод: оба алгоритма имеют линейную сложность. Использование функций min и max не позволило снизить сложность
# алгоритма ввиду того, что методы min и max внутри используют те же принципы, которые используются в алгоритме 1.
