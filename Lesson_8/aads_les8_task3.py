# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random

"""
Сначала не обратил внимание, что в условии задачи нужно написать функцию для создания ориентированного графа,
написал более сложный вариант для неориентированного, удалять было жалко.

def create_graph(size):
    graph = [[] for _ in range(size)]
    for i in range(size):
        for idx, line in enumerate(graph):
            if i in line:
                graph[i].append(idx)
        for j in range(i + 1, size):
            if j in graph[i]:
                continue
            spam = random.choice([1] + [0] * int(size / 5))
            if spam == 1:
                graph[i].append(j)
        if not graph[i]:
            graph[i].append(random.randint(i, size))

    return graph
"""


def create_graph(size):
    graph = [[] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if j == i:
                continue
            spam = random.choice([1] + [0] * int(size / 5))
            if spam == 1:
                graph[i].append(j)
        if not graph[i]:
            graph[i].append(random.randint(0, size))

    return graph


def depth_first_search(graph, start):

    if not is_visited[start]:
        is_visited[start] = True
        vertexes_found.append(start)

        for vertex in graph[start]:
            depth_first_search(graph, vertex)

    return vertexes_found


s = int(input('Сколько вершин будет в графе? '))
g = create_graph(s)
print(*g, sep='\n')

is_visited = [False] * len(g)
vertexes_found = []

begin = int(input('От какой вершины начать поиск в глубину? '))
print(f'Порядок обхода вершин при поиске в глубину:\n{depth_first_search(g, begin)}')
