import sys
input = sys.stdin.readline
from collections import deque

N, M, T = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
m = [list(map(int, input().split())) for _ in range(N)]
q = deque()
visited = [[0] * M for _ in range(N)]

def bfs():
    gram = 10001
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return min(visited[x][y]-1, gram)
        if m[x][y] == 2:
            gram = visited[x][y]-1 + N-1-x + M-1-y

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # print(x, y, nx, ny, visited[nx][ny], not visited[nx][ny])
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if m[nx][ny] == 0 or m[nx][ny] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # print(nx, ny)
    return gram

res = bfs()
if res > T:
    print('Fail')
else:
    print(res)