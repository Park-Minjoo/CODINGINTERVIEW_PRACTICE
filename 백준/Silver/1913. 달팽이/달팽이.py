import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = [[0]*n for _ in range(n)]

x, y = n//2, n//2
graph[x][y] = 1
repeat = 1
i = 0
num = 2
ans = [x+1, y+1]

while x != 0 or y != 0:
    flag = 0
    for _ in range(2): # 2번 반복
        for _ in range(repeat):
            x += dx[i]
            y += dy[i]
            graph[x][y] = num # 2
            if num == k: # 찾는 숫자면 저장
                ans = [x+1, y+1]
            if x == 0 and y == 0: # 마지막을 만나면
                flag = 1
                break
            num += 1 # 숫자 증가
        if flag == 1: break
        i = (i+1)%4 # 0 1 2 3 반복
    repeat += 1 # 반복 횟수 증가

for i in graph:
    print(*i, sep=' ')

print(*ans)

