n, m = map(int, input().split())

data = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]  # 벽을 세운 데이터를 바이러스를 퍼트릴 임시 테이블로 옮긴다.

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:  # 바이러스가 발견되면
                    virus(i, j)  # 바이러스를 퍼트리꼬
        result = max(result, get_score())  # 안전공간이 제일 많은곳으로 저장
        return
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                data[i][j] = 0

dfs(0)
print(result)