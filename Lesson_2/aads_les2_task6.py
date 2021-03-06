# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, вывести ответ.

from random import randint

num = randint(0, 100)
try_count = 0

while try_count < 10:
    answer = int(input('Попробуйте угадать число от 0 до 100: '))
    if answer == num:
        print('Вы угадали!')
        break
    elif answer > num:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
    try_count += 1

if try_count == 10:
    print(f'Вы не угадали, правильный ответ был: {num}')
