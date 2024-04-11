# graph representation using adjacency matrix


class Graph:
    def __init__(self , no_of_nodes) -> None:
        self.size = no_of_nodes
        self.graph = [[0 * no_of_nodes] * no_of_nodes]
    def add_edge(self, a, b, weight):
        if  a not in range(self.size) or b not in range(self.size):
            return
        self.graph[a][b] = weight    
        self.graph[b][a] = weight    

    def initialize_test_weighted_graph(self):
        # weighted graph ( see ../images/weighted_graph.png )
        return [
            [0, 4,  0,  0,  0,  0,  0, 8,  0],
            [4, 0,  8,  0,  0,  0,  0, 11, 0],
            [0, 8,  0,  7,  0,  4,  0, 0,  2],
            [0, 0,  7,  0,  9,  14, 0, 0,  0],
            [0, 0,  0,  9,  0,  10, 0, 0,  0],
            [0, 0,  4,  14, 10, 0,  2, 0,  0],
            [0, 0,  0,  0,  0,  2,  0, 1,  6],
            [8, 11, 0,  0,  0,  0,  1, 0,  7],
            [0, 0,  2,  0,  0,  0,  6, 7,  0]
        ]


