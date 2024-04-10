from queue import Queue

graph_map = {0:"A",1:"B",2:"C",3:"D",4:"E"}
'''
0---3---1
 \  |   |
  \ |   |
   \|   |
    4---2
'''
graph = [
    [0,0,0,1,1],
    [0,1,1,0,0],
    [0,1,0,0,1],
    [1,1,0,0,1],
    [1,0,1,1,0]
]
size = 5

def BFS(starting_node): # graph is an adjacency matrix
    visited = list()
    queue = Queue(size)
    # starting with first node
    print(starting_node)
    queue.put(starting_node)
    visited.append(starting_node)
    while not queue.empty():
        current_node = queue.get()
        for node in range(size):
            adjacent_node = graph[current_node][node] 
            if  adjacent_node == 1 and node not in visited:
                print(node)
                visited.append(node)
                queue.put(node)


if __name__ == "__main__":
    BFS(graph,5)