def floyd_warshall(matrix):
    count_vertex = len(matrix)
    
    # Initialize the shortest distances matrix
    for k in range(count_vertex):
        for i in range(count_vertex):
            for j in range(count_vertex):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    
    return matrix

# Example usage:
# Let's say we have the following weighted graph represented by an adjacency matrix
# 0: A, 1: B, 2: C, 3: D
# For simplicity, we represent infinity as a very large number, here we use 99999
graph = [
    [0, 5, 99999, 10],
    [99999, 0, 3, 99999],
    [99999, 99999, 0, 1],
    [99999, 99999, 99999, 0]
]

# Running Floyd-Warshall's algorithm on the graph
shortest_distances = floyd_warshall(graph)

# Output the shortest distances matrix
for row in shortest_distances:
    print(row)
