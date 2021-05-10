# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

friends_num = int(input('Сколько было друзей? '))
shake_num = 0

graph = [[1] * friends_num for _ in range(friends_num)]

for i in range(friends_num):
    graph[i][i] = 0
    for j in range(i, friends_num):
        shake_num += graph[i][j]

print(*graph, sep='\n')
print(f'\nВсего было {shake_num} рукопожатий')
