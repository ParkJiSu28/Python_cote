n =int(input())

cnt = 1

tmp =[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
       tmp[i][j] = cnt
       cnt +=1
    if i%2 == 1:
        tmp[i].reverse()

for i in tmp:
    for j in i:
        print(j,end=' ')
    print()