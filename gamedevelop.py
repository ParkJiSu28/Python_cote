n, m = map(int, input().split())

visit = [[0] * m for _ in range(n)]  # list컴프리헨션

x, y, direction = map(int, input().split())

visit[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


turn_count = 0
count = 1
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if visit[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        visit[nx][ny] = 1
        count += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(count)