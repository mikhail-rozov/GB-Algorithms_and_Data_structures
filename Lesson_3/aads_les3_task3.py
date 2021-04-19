# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и
# их аналогов, в том числе написанных самостоятельно.
# Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint

the_list = [randint(-100, 100) for _ in range(10)]
print(f'Первоначальный список:\n{the_list}')

max_number = min_number = the_list[0]

for number in the_list:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

if the_list.index(max_number) > the_list.index(min_number):
    the_list[the_list.index(max_number)] = min_number
    the_list[the_list.index(min_number)] = max_number
else:
    the_list[the_list.index(min_number)] = max_number
    the_list[the_list.index(max_number)] = min_number

print(f'Список, в котором минимальный и максимальный элементы поменяны местами:\n{the_list}')
