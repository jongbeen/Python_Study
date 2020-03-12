from heapq import heappush, heappop

INF = 1e9

def dijkstra(V,start,graph):
    dist = [INF] * V
    dist[start-1] = 0
    queue =[]
    heappush(queue, [0, start-1])
    
    while queue:
        cost , pos = heappop(queue)
        for p,c in graph[pos]:
            c += cost
            if c < dist[p]:
                dist[p] = c
                heappush(queue,[c,p])
    return dist


N = int(input())
M = int(input())
Graph = [[] for _ in range(N)]
for _ in range(M):
    u,v,w = list(map(int,input().split()))
    Graph[u-1].append([v-1,w])

S,E = list(map(int,input().split()))
Path = dijkstra(N,S,Graph)
print(Path[E-1])
