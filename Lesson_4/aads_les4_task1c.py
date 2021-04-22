# Измерить время работы кода при помощи timeit и cProfile.
# Результаты измерений сохранить в файл с кодом в виде комментариев.
# При необходимости, изменить исходный код.

# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
# Примечание: попытайтесь решить задания без использования функций max, min,
# sum, sorted и их аналогов, в том числе написанных самостоятельно.

from random import randint
import cProfile


def find_sum_between(n):
    numbers = [randint(-100, 100) for _ in range(n)]
    answer = 0

    # print(numbers)

    max_number = min_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number

    if numbers.index(max_number) > numbers.index(min_number):
        for number in numbers[numbers.index(min_number) + 1:numbers.index(max_number)]:
            answer += number
    else:
        for number in numbers[numbers.index(max_number) + 1:numbers.index(min_number)]:
            answer += number

    return answer


# "aads_les4_task1c.find_sum_between(100)"
# 1000 loops, best of 5: 53.5 usec per loop

# "aads_les4_task1c.find_sum_between(500)"
# 1000 loops, best of 5: 263 usec per loop

# "aads_les4_task1c.find_sum_between(1000)"
# 1000 loops, best of 5: 510 usec per loop

# cProfile.run('find_sum_between(100)')
# 535 function calls in 0.000 seconds
#       100    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#       100    0.000    0.000    0.000    0.000 random.py:290(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:334(randint)
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       126    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('find_sum_between(500)')
# 2651 function calls in 0.001 seconds
#       500    0.000    0.000    0.000    0.000 random.py:237(_randbelow_with_getrandbits)
#       500    0.000    0.000    0.000    0.000 random.py:290(randrange)
#       500    0.000    0.000    0.001    0.000 random.py:334(randint)
#       500    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#       642    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# cProfile.run('find_sum_between(1000)')
# 5309 function calls in 0.001 seconds
#      1000    0.000    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.000    0.000    0.001    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.001    0.000 random.py:334(randint)
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1300    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вывод: алгоритм имеют линейную сложность. Проверка алгоритма с использованием методов min, max и sum не произодилась
# ввиду того, что эти методы внутри работают по тем же принципам, что алгоритм 1. Данная проверка была проведена
# в задаче 1b, где использование методов не привело к снижению сложности алгоритма.
