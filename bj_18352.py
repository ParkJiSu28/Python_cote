import sys

input = sys.stdin.readline

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

dist = [-1] * (n + 1)
dist[x] = 0

for _ in range(m):
    i, j = list(map(int, input().split()))
    graph[i].append(j)

q = deque([x])

while q:
    now = q.popleft()
    for next in graph[now]:
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            q.append(next)

for i in range(n + 1):
    if dist[i] == k:
        print(i)

if k not in dist:
    print(-1)
