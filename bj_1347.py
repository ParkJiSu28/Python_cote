cnt = int(input())

note = input()
from collections import deque

# board = [[-1]*50 for _ in range(50)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 남 서 북 동
d = 2

x, y = 0, 0


def lota(ch, direction):
    if ch == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


x_list = [0]
y_list = [0]

for s in note:
    if s == 'F':
        nx = x + dx[d]
        ny = y + dy[d]
        x_list.append(nx)
        y_list.append(ny)
        x = nx
        y = ny
    elif s == 'R':
        d = lota(s, d)
    else:
        d = lota(s, d)

max_x, min_x, max_y, min_y = max(x_list), min(x_list), max(y_list), min(y_list)

n, m = max_x - min_x+1, max_y - min_y+1

start_x, start_y = abs(min_x), abs(min_y)

board = [['#'] * m for _ in range(n)]
for x, y in zip(x_list, y_list):
    board[start_x + x][start_y + y] = '.'


for i in board:
    print("".join(i))

