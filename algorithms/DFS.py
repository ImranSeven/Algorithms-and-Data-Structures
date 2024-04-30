def depth_first_search(graph, start):
    """
    Performs a depth-first search on a graph from a specified start node.

    Parameters:
    - graph (list of list of int): The graph, represented as a list where each index is a node and each element is a list of that node's neighbors.
    - start (int): The index of the starting node for the DFS traversal.

    Returns:
    - None: This function does not return a value but prints the order of traversal.
    """
    # Initialize a list to keep track of visited nodes, 
    # setting all elements to False indicating that no nodes have been visited yet.
    visited = [False] * len(graph)
    # Call the recursive helper function to visit the nodes.
    depth_first_search_recursive(graph, start, visited)     

def depth_first_search_recursive(graph, vertex, visited):
    # Mark the current node as visited.
    visited[vertex] = True
    # Print the node (for order of traversal).
    print(vertex)
    # For each neighbor of the current node, if the neighbor has not been visited yet, call the function recursively.
    for v in graph[vertex]:
        if not visited[v]:
            depth_first_search_recursive(graph, v, visited)

# Example usage:
graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
depth_first_search(graph, 0) # Output: 0 1 3 2