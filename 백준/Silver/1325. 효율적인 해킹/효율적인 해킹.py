from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    visited = [False] * (n+1)
    visited[start] = True

    while q:
        cur = q.popleft()
        for next in g[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt

res = []
for start in range(1, len(g)):
    res.append(bfs(start))

for i in range(len(res)):
    if max(res) == res[i]:
        print(i+1, end=" ")