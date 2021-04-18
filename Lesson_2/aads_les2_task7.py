# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Введите любое натуральное число: '))
a = 0

for i in range(n + 1):
    a += i

b = n * (n + 1) / 2

print(f'Выражение 1+2+...+n равно {a}')
print(f'Выражение n(n+1)/2 равно {b}')

if a == b:
    print("Равенство выполняется")
else:
    print("Равенство не выполняется")
