board = [[0]*10 for x in range(10)]

for x in range(10):
        board[x] = map(int,input().split())


for x in board:
    for y in x:
        print(y,end= ' ')
    print()