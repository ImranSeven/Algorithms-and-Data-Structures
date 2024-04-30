class ResidualNetwork:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.parent = [-1] * len(graph)

    def bfs(self, s, t):
        # Breadth-first search to find augmenting paths
        queue = []
        queue.append(s)
        self.visited = [False] * len(self.graph)
        self.parent = [-1] * len(self.graph)
        self.visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if self.visited[ind] == False and val > 0:
                    queue.append(ind)
                    self.visited[ind] = True
                    self.parent[ind] = u
        return self.visited[t]

    def get_AugmentingPath(self):
        # Backtrack from sink to source to find the augmenting path
        min_flow = float("inf")
        v = len(self.graph) - 1
        while v != 0:
            u = self.parent[v]
            min_flow = min(min_flow, self.graph[u][v])
            v = u
        v = len(self.graph) - 1
        # Update the flow along the augmenting path
        while v != 0:
            u = self.parent[v]
            self.graph[u][v] -= min_flow
            self.graph[v][u] += min_flow
            v = u
        return min_flow

    def has_AugmentingPath(self):
        # Check if there's an augmenting path from source to sink
        return self.bfs(0, len(self.graph) - 1)

    def augmentFlow(self):
        # Augment flow along the current augmenting path
        return self.get_AugmentingPath()


def ford_fulkerson(my_graph):
    # Initialise flow
    flow = 0
    # Initialise the residual network
    residual_network = ResidualNetwork(my_graph)
    # as long as there is an augmenting path
    while residual_network.has_AugmentingPath():
        # take the path
        path = residual_network.get_AugmentingPath()
        # augment the flow equal to the residual capacity
        flow += path
        # updating the residual network
        residual_network.augmentFlow()
    return flow


# Test cases
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

print("Maximum flow in the graph:", ford_fulkerson(graph))
