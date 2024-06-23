import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1 ,0, 0]

def BFS(x, y):
    queue = deque([(x, y)])
    visited[y][x] = True
    sheep, wolf = 0,0

    if graph[y][x] == 'o':
        sheep += 1
    elif graph[y][x] == 'v':
        wolf += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < C and 0 <= next_y < R:
                if not visited[next_y][next_x] and graph[next_y][next_x] != '#':
                    queue.append([next_x, next_y])
                    visited[next_y][next_x] = True
                    if graph[next_y][next_x] == 'o':
                        sheep += 1
                    elif graph[next_y][next_x] == 'v':
                        wolf += 1
    return (sheep, wolf)

def solve():
    total_sheep, total_wolf = 0, 0
    for x in range(C):
        for y in range(R):
            if graph[y][x] != '#' and not visited[y][x]:
                sheep, wolf = BFS(x, y)

                if sheep > wolf:
                    wolf = 0
                else:
                    sheep = 0
                total_sheep += sheep
                total_wolf += wolf
    print(total_sheep, end=' ')
    print(total_wolf, end=' ')

solve()