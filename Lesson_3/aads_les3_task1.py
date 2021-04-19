# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

divisor = 2

while divisor <= 9:
    div_count = 0
    for number in range(2, 100):
        if number % divisor == 0:
            div_count += 1
    print(f'Количество чисел в диапазоне [2; 99], кратных {divisor} - {div_count}')
    divisor += 1
