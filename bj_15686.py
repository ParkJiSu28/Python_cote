from itertools import combinations

n, m = map(int, input().split())

board = []
chicken = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 2:
            chicken.append((i, j))

example = []


def choice():
    for it in combinations(chicken, m):
        example.append(it)
    return example


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def sol(exam):
    answer = 1e9
    for ex in exam:
        ans = 0
        for x in range(n):
            for y in range(n):
                dist = 1e9
                if board[x][y] == 1:
                    for cal in ex:
                        tmp = abs(cal[0] - x) + abs(cal[1] - y)
                        dist = min(dist, tmp)
                    ans += dist
        answer = min(answer, ans)

    return answer


tmp = choice()
print(sol(tmp))

