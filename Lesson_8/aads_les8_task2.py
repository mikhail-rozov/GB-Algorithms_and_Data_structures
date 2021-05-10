# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

from collections import deque

g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra (graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    vertex_list = [deque() for _ in range(length)]
    vertex_list_start = start

    cost[start] = 0
    min_cost = 0

    # Функция для создания списка вершин, которые необходимо обойти при движении из стартовой вершины до
    # всех остальных.
    def get_vertex_list():

        for j in range(length):
            if j == vertex_list_start:
                vertex_list[j].appendleft(j)
                vertex_list[j].appendleft([j])
            else:
                spam = j
                if parent[j] == -1:
                    vertex_list[j].appendleft([j])
                    continue
                while spam != -1:
                    vertex_list[j].appendleft(spam)
                    spam = parent[spam]
                else:
                    vertex_list[j].appendleft([j])

        for idx, j in enumerate(vertex_list):
            vertex_list[idx] = list(j)
            if len(vertex_list[idx]) == 1:
                vertex_list[idx].append('нет пути')

        print(*vertex_list, sep='\n')

    #####################################################

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    get_vertex_list()
    print()
    return cost


s = int(input('От какой вершины идти? '))
print(dijkstra(g, s))
