# simple-max-flow
A basic implementation of the [Ford-Fulkerson maximum-flow algorithm](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) (FFA).

# Motivation
This algorithm is the first solution to the [maximum flow problem](https://en.wikipedia.org/wiki/Maximum_flow_problem), and the idea is to model a problem with a flow network and find a flow that fits the constraints but is as large as possible. FFA does this by repeatedly creating a residual graph and finding an available path for augmenting flow. Learning how FFA works provides a foundational understanding of maximum flow problems, of which translate nicely into real world problems like airline scheduling and baseball elimination. 

# How to use
Add your flow network by inputing its edges, flows, and capacities in ``edges``. An edge follows the format ``[u,v,c(e),f(e)]...e = (u,v) edge, c(e) capacity, f(e) flow``. Nodes are numbers ``0,1,2,...`` and the source or start node is ``0``.

Run ``python main.py`` and see your output!
