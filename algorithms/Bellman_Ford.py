def bellman_ford(vertices, edges, source):
    # Step 1: Initialize the graph
    distance = {}
    predecessor = {}
    for vertex in vertices:
        if vertex == source:
            distance[vertex] = 0
        else:
            distance[vertex] = float('inf')
        predecessor[vertex] = None

    # Step 2: Relax edges repeatedly
    for _ in range(len(vertices) - 1):
        for edge in edges:
            u, v, w = edge
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    # Step 3: Check for negative-weight cycles
    for edge in edges:
        u, v, w = edge
        if distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return distance, predecessor

# Example usage:

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B', 6), ('A', 'D', 7), ('B', 'C', 5), ('B', 'D', 8), ('B', 'E', -4), ('C', 'B', -2), ('D', 'C', -3), ('D', 'E', 9), ('E', 'C', 7)]
source = 'A'
distance, predecessor = bellman_ford(vertices, edges, source)
print("Distance:", distance)
print("Predecessor:", predecessor)
# Distance: {'A': 0, 'B': 2, 'C': 4, 'D': 7, 'E': -2}
# Predecessor: {'A': None, 'B': 'C', 'C': 'E', 'D': 'A', 'E': 'B'}

vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 3), ('B', 'C', 1), ('C', 'D', -10)]
source = 'A'
distance, predecessor = bellman_ford(vertices, edges, source)
print("Distance:", distance)
print("Predecessor:", predecessor)
# Distance: {'A': 0, 'B': 3, 'C': 4, 'D': -6}
# Predecessor: {'A': None, 'B': 'A', 'C': 'B', 'D': 'C'}
