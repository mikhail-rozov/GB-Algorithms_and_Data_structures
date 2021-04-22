# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile


# Функция для проверки правильности нахождения простого числа:
def test_prime(func):
    test_sequence = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, number in enumerate(test_sequence):
        assert number == func(i)
        print(f'Test # {i + 1} OK!')


# Решение с помощью алгоритма "Решето Эратосфена":
def sieve(n):

    seq_length = n * 10 + 10
    sequence = [i for i in range(seq_length)]
    sequence[1] = 0

    for i in range(2, seq_length):
        if sequence[i] != 0:
            j = i * 2

            while j < seq_length:
                sequence[j] = 0
                j += i

    sequence = [i for i in sequence if i != 0]
    return sequence[n]


# Нахождение простого числа классическим способом:
def prime(n):

    seq_length = n * 10 + 10
    sequence = [i for i in range(2, seq_length)]
    prime_sequence = sequence.copy()

    for i, number in enumerate(sequence):
        for el in sequence[:i]:
            if number % el == 0:
                prime_sequence.remove(number)
                break

    return prime_sequence[n]


# test_prime(sieve)
# test_prime(prime)

# Анализ скорости и сложности алгоритма                     Анализ скорости и сложности алгоритма
# "Решето Эратосфена":                                      нахождения простого числа классическим способом:
# ----------------------------------------                   -----------------------------------------------

# "aads_les4_task2.sieve(50)"                               "aads_les4_task2.prime(50)"
# 1000 loops, best of 5: 76 usec per loop                   1000 loops, best of 5: 1.05 msec per loop

# "aads_les4_task2.sieve(100)"                              "aads_les4_task2.prime(100)"
# 1000 loops, best of 5: 155 usec per loop                  1000 loops, best of 5: 3.57 msec per loop

# "aads_les4_task2.sieve(300)"                              "aads_les4_task2.prime(300)"
# 1000 loops, best of 5: 482 usec per loop                  1000 loops, best of 5: 28.4 msec per loop

# "aads_les4_task2.sieve(1000)"                             слишком долго...
# 1000 loops, best of 5: 1.68 msec per loop

# cProfile.run("sieve(50)")                                 cProfile.run("prime(50)")
# 6 function calls in 0.000 seconds                         417 function calls in 0.001 seconds
#                                                           411    0.000    0.000    0.000    0.000
#                                                           {method 'remove' of 'list' objects}

# cProfile.run("sieve(100)")                                cProfile.run("prime(100)")
# 6 function calls in 0.000 seconds                         845 function calls in 0.004 seconds
#                                                           839    0.001    0.000    0.001    0.000
#                                                           {method 'remove' of 'list' objects}

# cProfile.run("sieve(1000)")                               cProfile.run("prime(1000)")
# 6 function calls in 0.002 seconds                         8783 function calls in 0.329 seconds
#                                                           8777    0.057    0.000    0.057    0.000
#                                                           {method 'remove' of 'list' objects}

# cProfile.run("sieve(5000)")                               cProfile.run("prime(5000)")
# 6 function calls in 0.011 seconds                         44881 function calls in 10.258 seconds
#                                                           44875    1.237    0.000    1.237    0.000
#                                                           {method 'remove' of 'list' objects}

# Вывод: алгоритм нахождения простого числа с помощью "решета Эратосфена" имеет линейную сложность, тогда как
# классический алгоритм, в котором каждое число списка делится на все предыдущие числа до тех пор, пока остаток
# от деления не будет равен нулю, имеет квадратичную сложность.
