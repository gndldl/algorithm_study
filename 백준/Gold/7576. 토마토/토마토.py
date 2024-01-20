from collections import deque


m, n = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 1:
            q.append((i, j))
    graph.append(line)

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs()
max_n = 0
able = True
for i in graph:
    for j in i:
        if j == 0:
            able = False
            break
    max_n = max(max_n, max(i))

if able:
    print(max_n - 1)
else:
    print(-1)