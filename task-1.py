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

# Візуалізація графу
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
plt.title("Social Network Graph")
plt.show()

# Аналіз основних характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())

print("Кількість вузлів (людей):", num_nodes)
print("Кількість ребер (зв'язків):", num_edges)
print("Ступені вузлів (кількість друзів кожної людини):", degree_dict)
