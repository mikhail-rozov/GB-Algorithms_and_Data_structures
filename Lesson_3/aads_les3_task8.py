# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# Примечание: попытайтесь решить задания без использования функций
# max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно.

matrix = [[int(input('Введите очередной элемент матрицы: ')) for _ in range(4)] for _ in range(4)]

for line in matrix:
    sum_line = 0
    for number in line:
        sum_line += number
    line.append(sum_line)

for line in matrix:
    for number in line:
        print(f'{number:>5}', end='')
    print()