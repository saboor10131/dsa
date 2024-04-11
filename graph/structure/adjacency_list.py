# graph representation using adjacency list


class Graph:
    def __init__(self):
        self.graph = dict()      
    
    def add_edge(self,a,b,weight=0):
        if a not in self.graph:
            self.graph[a] = list()
        if b not in self.graph:
            self.graph[b] = list()

        self.graph[a].append((b,weight))    
        self.graph[b].append((a,weight))  
    
    def initialize_test_weighted_graph(self):

        # weighted graph ( see ../images/weighted_graph.png )
        self.graph = {
            "0"  : [ (1,4), (7,8)  ],  # edge between 0 and 1 with weight 4
            "1"  : [ (0,4), (2,8)   , (7,11)],
            "2"  : [ (1,8), (3,7)   , (5,4)  , (8,2)],
            "3"  : [ (2,7), (4,9)   , (5,14)],
            "4"  : [ (3,9), (5,10) ],
            "5"  : [ (2,4), (3,14)  , (4,10) , (6,2)],
            "6"  : [ (5,2), (7,1)   , (8,6) ],
            "7"  : [ (0,8), (1,11)  , (6,1)  , (8,7)],
            "8"  : [ (2,2), (7,7)  ]
        }
        
        return self.graph 


    
