import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вузлів (людей)
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah']
G.add_nodes_from(people)

# Додавання ребер (дружніх зв’язків)
friendships = [
    ('Alice', 'Bob'),
    ('Alice', 'Charlie'),
    ('Alice', 'David'),
    ('Bob', 'Charlie'),
    ('Bob', 'Eve'),
    ('Charlie', 'Frank'),
    ('David', 'Eve'),
    ('Eve', 'Frank'),
    ('Frank', 'Grace'),
    ('Grace', 'Hannah')
]
G.add_edges_from(friendships)

# Функція для пошуку шляхів за допомогою DFS
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            new_path = dfs_path(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# Функція для пошуку шляхів за допомогою BFS
def bfs_path(graph, start, goal):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for adjacent in graph.neighbors(node):
            if adjacent not in path:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    return None

# Пошук шляхів за допомогою DFS та BFS
start_node = 'Alice'
goal_node = 'Hannah'

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

# Виведення результатів
print("Шлях від", start_node, "до", goal_node, "за допомогою DFS:", dfs_result)
print("Шлях від", start_node, "до", goal_node, "за допомогою BFS:", bfs_result)

# Візуалізація графу
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Social Network Graph")
plt.show()

