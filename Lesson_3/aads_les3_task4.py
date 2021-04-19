# Определить, какое число в массиве встречается чаще всего.
# Если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint

numbers = [randint(0, 4) for _ in range(10)]
num_count = 0
print(f'Дан список:\n{numbers}')

for number in numbers:
    if numbers.count(number) > num_count:
        num_count = numbers.count(number)

for number in numbers:
    if numbers.count(number) == num_count:
        print(f'\nЧаще всего в этом списке встречается число {number} - {num_count} раз(а)')
        break
