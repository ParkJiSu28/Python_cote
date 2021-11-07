from collections import deque

## dfs,bfs 둘다 상관없다
## 한개의 노드를 시작점으로 잡고 다른 노드를 방문할 수 있는 만큼 방문한다
## 한번의 방문 할 수 있는 탐색방법 하나가 네트워크 한개이다.
## 따라서 각 노드마다 방문하지 않는 노드를 선택해서 방문한다면 탐색방법의 가짓수가 나온다.

n = 3
computers = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for next in range(n):
        if not visited[next]:
            dfs(n, computers, next, visited)  # bfs(n,computers,next,visited)
            answer += 1
    print(answer)
    return answer


def dfs(n, computers, start, visited):
    visited[start] = True
    for next in range(n):
        if next != start and computers[start][next] == 1:
            if visited[next] == False:
                bfs(n, computers, next, visited)


def bfs(n, computers, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        start = q.popleft()
        visited[start] = True
        for next in range(n):
            if next != start and computers[start][next] == 1:
                if visited[next] == False:
                    q.append(next)


solution(n,computers)