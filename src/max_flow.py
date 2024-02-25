# max_flow.py
# Has the maximum flow (Ford–Fulkerson) algorithm and related helper functions
# Scott Renegado

from graph import Graph

def bfs(graph, start, end):
    """
    Basic BFS that returns the BFS path from start node to end node.
    https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
    """
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    discovered = {start}
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get_adjacencies(node):
            if adjacent[0] not in discovered:
                discovered.add(adjacent[0])
                new_path = list(path)
                new_path.append(adjacent[0])
                queue.append(new_path)        


def build_residual_graph(G):
    """
    Build residual graph G_f from G.
    Convention: forward edges have flow 0 and backward edges have flow 1.
    """
    G_f = Graph(G.size_n())

    # Iterate edges of G
    for node,adjs in G.get_adj_list().items():
        for adj in adjs: # edge e = (u,v)
            if adj[2] < adj[1]: # flow(e) < capacity(e)

                # Add edge (u,v) with capacity c(u,v) = c(e) - f(e) 
                forward_edge = (node, adj[0], adj[1] - adj[2], 0)
                G_f.add_edge(*forward_edge)

            if adj[2] > 0: # flow(e) > 0

                # Add edge (v,u) with capacity c(v,u) = f(e) 
                backward_edge = (adj[0], node, adj[2], 1)
                G_f.add_edge(*backward_edge) 

    return G_f


def bottleneck(P, G_f):
    """
    Find minimal residual capacity in augmenting path P from residuel graph G_f.
    """
    b = float('inf') # bottleneck

    # Traverse P in G_f
    for i in range(len(P)-1):
        for adj in G_f.get_adjacencies(P[i]):
            if adj[0] == P[i+1] and b > adj[1]:
                # Edge e in path P found and bottleneck > capacity(e)
                 
                b = adj[1] # Set bottleneck to capacity(e)
    return b


def augment(P, G, G_f):
    """
    Augment flow in G from P and G_f.
    """
    b = bottleneck(P, G_f)

    # Traverse P in G_f
    for i in range(len(P)-1):
        for adj_f in G_f.get_adjacencies(P[i]):
            if adj_f[0] == P[i+1]: 
                if adj_f[2] == 0: # e is a forward edge
                    G.augment_flow(P[i], P[i+1], b)
                elif adj_f[2] == 1: # e is a backward edge
                    G.augment_flow(P[i], P[i+1], -b)


def ford_fulkerson(G):
    """
    Return G with max-flow.
    """
    G_f = build_residual_graph(G)
    path_in_Gf = True

    while path_in_Gf:
        # Find an augmenting path P in G_f
        P = bfs(G_f, 0, G_f.size_n()-1)

        if P != None:
            augment(P, G, G_f)
            G_f = build_residual_graph(G)
        else:
            path_in_Gf = False

    return G

def compute_max_flow(Gmax, start):
    """
    Compute max flow from Gmax.
    """
    max_flow_val = 0

    # Sum all the flow from edges coming out of start node
    for adj in Gmax.get_adjacencies(start):
        adjacent_flow = adj[2]
        max_flow_val += adjacent_flow

    return max_flow_val