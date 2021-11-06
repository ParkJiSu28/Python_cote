# dfs version
from collections import deque

n, m = map(int, input().split())

graph = []
graph2 = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        graph2[i][j] = graph[i][j]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


# bfs version
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph2[nx][ny] == 0:
                graph2[nx][ny] = 1
                queue.append((nx, ny))


result = 0
bfs_result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j): # dfs연결요소 찾기
            result += 1
        if graph2[i][j] == 0: # bfs 연결요소 찾기
            bfs(i, j)
            bfs_result += 1

print(result)
print(bfs_result)
