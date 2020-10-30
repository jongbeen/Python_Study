from collections import deque
import sys

sys.stdin = open('input_7576.txt', 'r')
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def BFS(graph):
    visited = [[False] * N for _ in range(M)]
    queue = deque(start_point)
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for nx, ny in zip(dx, dy):
            idx, idy = x + nx, y + ny
            if 0 <= idx < M and 0 <= idy < N:
                if graph[idx][idy] != -1 and not visited[idx][idy]:
                    graph[idx][idy] = graph[x][y] + 1
                    queue.append((idx, idy))
    return graph

N, M = map(int, input().split())
graph = [[0] * N for _ in range(M)]
start_point = []

for i in range(M):
    graph[i] = list(map(int, input().split()))

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            start_point.append((i, j))
graph = BFS(graph)
M, check = -2, True

for i in graph:
    if max(i) > M:
        M = max(i)
    if 0 in i:
        check = False
        break
if check:
    if M == -1:
        print(0)
    else:
        print(M - 1)
else:
    print(-1)
