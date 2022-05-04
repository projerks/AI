from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def BFS(self, s):

		visited = [False] * (max(self.graph) + 1)

		queue = []

		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print (s, end = " ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
v = int(input('Enter no. of vertices '))
edges = int(input('Enter no. of edges '))
for i in range(edges):
    x,y = input().split(" ")
    g.addEdge(int(x),int(y))

start = int(input('Enter start node '))

g.BFS(start)

# Enter No. of vertices 6
# Enter No. of edges 8
# 2 2
# 3 2
# 3 4
# 4 8
# 5 3
# 5 7
# 7 8
# 8 8
# enter start node 5
# 5 3 7 2 4 8 