# Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число: '))
result = ''

while num // 10 != 0:
    result += str(num % 10)
    num //= 10

result += str(num)
print(f'Число, обратное по порядку входящих в него цифр - {result}')
