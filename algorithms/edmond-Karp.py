from collections import deque

class Edge:
    def __init__(self, s, t, cap, rev):
        self.s = s  # source vertex
        self.t = t  # sink vertex
        self.cap = cap  # capacity
        self.flow = 0  # flow initialized to 0
        self.rev = rev  # reverse edge

class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]
        self.vertices = vertices

    def add_edge(self, s, t, cap):
        forward_edge = Edge(s, t, cap, None)
        backward_edge = Edge(t, s, 0, forward_edge)
        forward_edge.rev = backward_edge
        self.graph[s].append(forward_edge)
        self.graph[t].append(backward_edge)

def bfs(graph, s, t, pred):
    q = deque([s])
    pred[:] = [None] * len(graph.graph)
    while q:
        cur = q.popleft()
        for e in graph.graph[cur]:
            if pred[e.t] is None and e.t != s and e.cap > e.flow:
                pred[e.t] = e
                q.append(e.t)
                if e.t == t:
                    return True
    return False

def edmonds_karp(graph, s, t):
    flow = 0
    pred = [None] * len(graph.graph)
    
    while bfs(graph, s, t, pred):
        df = float('inf')
        e = pred[t]
        while e is not None:
            df = min(df, e.cap - e.flow)
            e = pred[e.s]
        
        e = pred[t]
        while e is not None:
            e.flow += df
            e.rev.flow -= df
            e = pred[e.s]
        
        flow += df
    
    return flow

#Example usage:
g = Graph(6)  # create a graph with 6 vertices
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

max_flow = edmonds_karp(g, 0, 5)
print(f"Maximum flow: {max_flow}")
