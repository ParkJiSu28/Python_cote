from collections import deque

n, k = map(int, input().split())

board = []
data = []

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            data.append((board[i][j], 0, i, j))

S, X, Y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

data.sort()
q = deque(data)

while q:
    virus, s, x, y = q.popleft()
    if s == S:
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 0:
                board[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(board[X - 1][Y - 1])