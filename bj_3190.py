from collections import deque

n = int(input())
m = int(input())

board = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1  # 사과

cnt = int(input())

q = deque()
for j in range(cnt):
    c, d = input().split()
    q.append((int(c), d))  # 3 D
# C왼쪽 D 오른쪽  0 : 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

SNAKE = -1

time = 0


def lotate(ch, direction):
    if ch == 'L':
        direction = (direction - 1) % 4
    else :
        direction = (direction + 1) % 4

    return direction


time = 0

tail = deque()
tail.append((1, 1))

c = 'D'  # 처음은 오른쪽으로 간다. 즉 동쪽 방향을 본다
d = 0
board[1][1] = SNAKE


x, y = 1, 1

while True:
    nx = x + dx[d]
    ny = y + dy[d]

    # 사과체크 및 이동 및 꼬리 체크
    if (nx < 1 or nx > n or ny < 1 or ny > n) or board[nx][ny] == SNAKE:  # 벽에 부딪히거나 자신의몸과 닿으면 게임 끝
        time += 1
        break
    elif board[nx][ny] == 1 and 1 <= nx <= n and 1 <= ny <= n:
        board[nx][ny] = SNAKE
        tail.append((nx, ny))  # 머리는 추후 꼬리가 됨으로 삽입

    elif board[nx][ny] == 0 and 1 <= nx <= n and 1 <= ny <= n:
        board[nx][ny] = SNAKE
        # 꼬리가 어디 방향으로 가는지 확인하여야함
        a, b = tail.popleft()
        board[a][b] = 0  # 꼬리 치워짐으로 인해 뱀인 구역 아님
        tail.append((nx, ny))

    x = nx
    y = ny
    time += 1  # 시간증가

    if q :  # 뱡향변화가 있는지 체크
        if q[0][0] == time:
            sec, c = q.popleft()
            d = lotate(c, d)

print(time)
