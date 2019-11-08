from collections import defaultdict

class Graph():
    def __init__(self,n):
        self.nodes = n
        self.adjList = defaultdict(list)

    def connect(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def find_all_distances(self, s):
        levels = [-1]*self.nodes
        visited = [0]*self.nodes
        queue = []
        queue.append(s)
        visited[s] = 1
        levels[s] = 0
        while len(queue)>0:
            u = queue.pop(0)
            for v in self.adjList[u]:
                if visited[v] == 0:
                    queue.append(v)
                    levels[v] = levels[u]+1
                    visited[v] = 1
        for idx,val in enumerate(levels):
            if idx!=s:
                if val != -1:
                    print(val*6,end=' ')
                else:
                    print(val,end=' ')

t = int(input())

for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    print()

