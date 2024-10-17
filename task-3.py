import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графу
G = nx.Graph()

# Додавання вузлів (людей)
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah']
G.add_nodes_from(people)

# Додавання ребер (дружніх зв’язків) з вагами
friendships_with_weights = [
    ('Alice', 'Bob', 1),
    ('Alice', 'Charlie', 2),
    ('Alice', 'David', 3),
    ('Bob', 'Charlie', 1),
    ('Bob', 'Eve', 4),
    ('Charlie', 'Frank', 3),
    ('David', 'Eve', 2),
    ('Eve', 'Frank', 1),
    ('Frank', 'Grace', 2),
    ('Grace', 'Hannah', 4)
]
G.add_weighted_edges_from(friendships_with_weights)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_path_tree = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node

    return distances, shortest_path_tree

# Застосування алгоритму Дейкстри
start_node = 'Alice'
distances, shortest_path_tree = dijkstra(G, start_node)

# Виведення результатів
print(f"Найкоротші відстані від {start_node}:")
for node, distance in distances.items():
    print(f"{node}: {distance}")

print("\nШляхи до кожного вузла:")
for node in shortest_path_tree:
    path = []
    current = node
    while current != start_node:
        path.append(current)
        current = shortest_path_tree[current]
    path.append(start_node)
    path.reverse()
    print(f"{node}: {' -> '.join(path)}")

# Візуалізація графу з вагами
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Social Network Graph with Weighted Connections")
plt.show()
