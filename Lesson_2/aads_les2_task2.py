# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

even_count = 0
odd_count = 0

for digit in num:
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'В числе {num} {even_count} чётных и {odd_count} нечётных цифр')
