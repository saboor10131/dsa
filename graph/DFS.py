graph_map = {0:"A",1:"B",2:"C",3:"D",4:"E"}
visited = []
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
def DFS(current_node): # graph is an adjacency matrix
    visited.append(current_node)
    print(current_node)
    for node in range(size):
        if graph[current_node][node] == 1 and node not in visited:
            DFS(node)


if __name__ == "__main__":
    DFS(0)