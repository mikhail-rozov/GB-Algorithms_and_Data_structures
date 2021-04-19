# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
# Примечание: попытайтесь решить задания без использования функций max, min,
# sum, sorted и их аналогов, в том числе написанных самостоятельно.

from random import randint

numbers = [randint(-20, 20) for _ in range(10)]

print(f'Дан список:\n{numbers}\n')

for i in range(2):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    numbers.remove(min_number)
    print(f'{i + 1}-ый наименьший элемент списка - {min_number}')
