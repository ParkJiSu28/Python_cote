n,m = map(int,input().split())

x ,y, d =map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))

visit = [[0]*m for i in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0

visit[x][y] =1

count = 1

turn_time = 0

def turn_left():
    global d
    if d== 0:
        d =3
    elif d%4 != 0:
        d -=1


while True:
    turn_left()
    nx = x +dx[d]
    ny = y +dy[d]
    if visit[nx][ny] == 0 and board[nx][ny] == 0:
        visit[nx][ny] =1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time ==4:
        nx = x -dx[d]
        ny = y -dy[d]

        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0


for visit_cnt in visit:
    print(visit_cnt)