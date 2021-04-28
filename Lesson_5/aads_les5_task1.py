# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

enterprises = defaultdict(int)
quantity = int(input('Сколько предприятий будем вводить? '))
total_profit = 0

for i in range(quantity):

    name = input(f'Введите название {i + 1}-го предприятия: ')
    profit = int(input('Введите прибыль этого предприятия за 4 квартала: '))
    enterprises[name] = profit

for val in enterprises.values():
    total_profit += val

average_profit = total_profit / quantity

above_average = [name for name in enterprises.keys() if enterprises[name] >= average_profit]
below_average = [name for name in enterprises.keys() if enterprises[name] < average_profit]

print(f'\nСредняя прибыль предприятий: {average_profit}')
print(f'\nПредприятия, у которых прибыль за 4 квартала выше средней:')
print(*above_average, sep='\n')
print(f'\nПредприятия, у которых прибыль за 4 квартала ниже средней:')
print(*below_average, sep='\n')
