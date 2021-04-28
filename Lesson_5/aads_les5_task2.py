# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
# каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче
# под запретом.

from collections import OrderedDict


def add(x, y):

    x = x[::-1]
    y = y[::-1]
    result = []
    ham = 0

    for _ in range(len(y) - len(x)):
        x.append('0')
    for _ in range(len(x) - len(y)):
        y.append('0')

    for i in range(len(x)):
        spam = hex_numbers[x[i]] + hex_numbers[y[i]] + ham
        ham = 0
        if spam > 15:
            spam -= 16
            ham += 1
        for key, val in hex_numbers.items():
            if spam == val:
                result.append(key)
                break

    if ham != 0:
        for key, val in hex_numbers.items():
            if ham == val:
                result.append(key)
                break

    result = result[::-1]
    return result


def multiply(m, n):

    factor = 0
    product = m.copy()
    n = n[::-1]

    for i, el in enumerate(n):
        factor += hex_numbers[el] * 16 ** i

    for _ in range(factor - 1):
        product = add(product, m)

    return product


hex_numbers = OrderedDict({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                           '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                           'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})

a = input('Введите первое число: ')
b = input('Введите второе число: ')

a = [el.upper() for el in a]
b = [el.upper() for el in b]

print(f'\nСумма этих чисел равна:\n{add(a, b)}')
print(f'\nПроизведение этих чисел равно:\n {multiply(a, b)}')
