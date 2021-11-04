board = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    list(map(int,input().split))



for i in range(h):
    for j in range(w):
        print(board[i][j], end=' ')
    print()
