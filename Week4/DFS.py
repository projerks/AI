from collections import defaultdict

class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# A function used by DFS
	def DFSUtil(self, v, visited):

		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)

	def DFS(self, v):

		visited = set()

		self.DFSUtil(v, visited)

# Driver code

g = Graph()
v = int(input('Enter no. of vertices '))
edges = int(input('Enter No. of edges '))
for i in range(edges):
    x,y = input().split(" ")
    g.addEdge(int(x),int(y))

start = int(input('Enter start node '))
g.DFS(start)
