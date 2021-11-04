n = int(input())

arr = [0 for x in range(n)]
for i in range(n):
    arr[i] = int(input())

ans = [[0]*n for x in range(n)]

for i in range(n):
    for j in range(i+1):
        if j == 0:
            ans[i][j] = arr[i]
        else:
            ans[i][j] = ans[i][j-1] - ans[i-1][j-1]

for i in ans:
    for j in i:
        if j != 0:
            print(j,end=' ')
    print()
