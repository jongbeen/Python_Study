# 내 풀이- 나는 되는데 틀렸다고 함 ㅠ
import heapq


def dijkstra(graph,start):
    distances = {node : float("INF") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[distances[start],start])
    
    while queue:
        current_distance,current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
        
        if graph[current_node] != float('inf'):
            for adjacent, weight in graph[current_node].items():
                distance = current_distance+weight
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue,[distance,adjacent])
    return distances


V,E = list(map(int,input().split()))
Start = input()

mygraph = dict()

for i in range(1,V+1):
    mygraph[str(i)] = dict()

for _ in range(E):
    u,v,w = input().split()
    w = int(w)
    mygraph[u][v] = w

ans = dijkstra(mygraph,Start)

for i in ans.values():
    if i==float('inf'):
        print("INF")
    else:
        print(i)
