# Закодируйте любую строку по алгоритму Хаффмана.

from binarytree import Node
from collections import deque, defaultdict

text = input('Введите строку для кодирования: ')

char_table = defaultdict(int)

for el in text:
    char_table[el] += 1

char_table = dict(char_table)

queue = deque(char_table.items())

while len(queue) > 1:
    queue = deque(sorted(queue, key=lambda x: x[1]))
    spam = Node(queue[0][1] + queue[1][1])
    if isinstance(queue[0][0], str):
        spam.left = Node(ord(queue[0][0]))
    else:
        spam.left = queue[0][0]
    if isinstance(queue[1][0], str):
        spam.right = Node(ord(queue[1][0]))
    else:
        spam.right = queue[1][0]
    queue.popleft()
    queue[0] = (spam, spam.value)

my_tree = queue[0][0]
result = None


def search(graph, char, in_binary=''):
    global result
    if graph.value == ord(char):
        result = in_binary
    if graph.left:
        search(graph.left, char, in_binary=f'{in_binary}0')
    if graph.right:
        search(graph.right, char, in_binary=f'{in_binary}1')
    return result


for key in char_table.keys():
    char_table[key] = search(my_tree, key)

coded_text = ''

for el in text:
    coded_text += char_table[el] + ' '

print(f'Закодированная строка имеет вид:\n{coded_text}')
