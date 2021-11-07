from collections import deque

numbers = [1, 1, 1, 1, 1]
target = 3


def bfs(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx < len(numbers):
            q.append([tmp + numbers[idx], idx])
            q.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer


def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        # 종료조건
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer
