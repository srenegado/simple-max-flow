# main.py
# Basic driver code with example graph.
# Scott Renegado

from graph import Graph
from max_flow import ford_fulkerson
from max_flow import compute_max_flow

def main():
    num_nodes = 6
    G = Graph(num_nodes)

    # Input: [u,v,c(e),f(e)]...e = (u,v) edge, c(e) capacity, f(e) flow
    # Example used: https://www.youtube.com/watch?v=Tl90tNtKvxs
    edges = [[0,1,10,0],[0,3,10,0],[1,2,4,0],[1,3,2,0],[1,4,8,0],[3,4,9,0],[4,2,6,0],[2,5,10,0],[4,5,10,0]] 

    G.add_edges(edges)
    print("Input flow network G:")
    G.print_adj_list()
    
    Gmax = ford_fulkerson(G)
    print("Flow network with max flow G_max:")
    Gmax.print_adj_list()

    max_flow_val = compute_max_flow(Gmax, 0)
    print("max-flow value of G =",max_flow_val)

if __name__ == '__main__':
    main()