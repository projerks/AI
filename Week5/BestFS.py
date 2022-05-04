from queue import PriorityQueue
 
# Function For Implementing Best First Search
# Gives output path having lowest cost
 

def best_first_search(source, target, n):
    visited = [0] * n
    visited[source] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        
        print(u, end=" ")
        if u == target:
            break

        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()

# Function for adding edges to graph


def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

v = int(input('Enter no. of vertices '))
graph = [[] for i in range(v)]
for i in range(v-1):
    x,y,z = input().split(" ")
    addedge(int(x),int(y),int(z))
 
 
# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
 
source = int(input('Enter source: '))

target = int(input('Enter target: '))

best_first_search(source, target, v)



# Enter no. of vertices 14
# 0 1 3
# 0 2 6
# 0 3 5
# 1 4 9
# 1 5 8
# 2 6 12
# 2 7 14
# 3 8 7
# 8 9 5
# 8 10 6
# 9 11 1
# 9 12 10
# 9 13 2
# Enter source: 0
# Enter target: 9
# 0 1 3 2 8 9
