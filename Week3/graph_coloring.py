# class to represent a graph object
class Graph:

    # Constructor
    def __init__(self, edges, N):
        
        self.adj = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)


# Function to assign colors to vertices of graph
def colorGraph(graph):

    # stores color assigned to each vertex
    result = {}

    # assign color to vertex one by one
    for u in range(N):

        # set to store color of adjacent vertices of u
        # check colors of adjacent vertices of u and store in set
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])

        # check for first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        # assigns vertex u the first available color
        result[u] = color

    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])


    # Add more colors for graphs with many more vertices
colors = [ "MAUVE","BLUE","GREEN","RED","YELLOW","ORANGE","PINK","BLACK","BROWN","WHITE",
          "PURPLE","VIOLET"]

N = int(input("Enter no of vertices: "))
edges = list(tuple(map(int,input().split())) for r in range(N))  

graph = Graph(edges, N)
    # color graph using greedy algorithm
colorGraph(graph)