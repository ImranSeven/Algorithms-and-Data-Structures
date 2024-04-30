def ford_fulkerson(my_graph):
    # Initialise flow
    flow = 0
    # Initialise the residual network
    residual_network = ResidualNetwork(my_graph)
    # as long as there is a augmenting path
    while residual_network.has_AusmentingPath():
        # take the path
        path = residual_network.get_AugmentingPath()
        # augment the flow equal to the residual capacity
        flow += path.residual_capacity
        # updating the residual network
        residual_network.augmentFlow(path)
    return flow