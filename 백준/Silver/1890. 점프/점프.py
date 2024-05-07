import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# print(graph)
direction = [(1, 0), (0, 1)] # 하, 우
dp = [[-1]*n for _ in range(n)]
# print(dp)
def dfs(x, y):
    if x == n-1 and y == n-1:
        # print('x == n-1 and y == n-1')
        return 1
    if dp[x][y] != -1:
        # print('dp[x][y] != -1', dp[x][y])
        return dp[x][y]
    else:
        dp[x][y] = 0
        # print('dp[', x, '][', y,'] = 0')
        for d in direction:
            nx = x + d[0] * graph[x][y]
            ny = y + d[1] * graph[x][y]
            # print('nx = x + d[0] * graph[x][y]')
            # print(nx, '=', x, '+', d[0], '*', graph[x][y])
            # print('ny = y + d[1] * graph[x][y]')
            # print(ny, '=', y, '+', d[1], '*', graph[x][y])

            if 0 <= nx < n and 0 <= ny < n:
                dp[x][y] += dfs(nx, ny)
                # print('dp[',x,'][',y,'] =', dp[x][y], 'nx, ny =', nx, ny)
    return dp[x][y]

print(dfs(0, 0))