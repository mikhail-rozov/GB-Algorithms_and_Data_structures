# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
# Примечание: попытайтесь решить задания без использования функций max, min,
# sum, sorted и их аналогов, в том числе написанных самостоятельно.
# Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint

numbers = [randint(-100, 100) for _ in range(10)]
answer = 0

print(f'Дан список:\n{numbers}')

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

print(f'\nСумма элементов списка между минимальным значением {min_number} и максимальным значением {max_number} '
      f'составляет {answer}')
