from collections import deque

n = int(input())
graph = []
answer = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = deque()
    q.append((x, y))
    cnt = 1
    graph[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))
            

answer.sort()
print(len(answer))
for i in answer:
    print(i)