import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

board = [0] * 101 # 1~100번째 칸 방문 횟수
visited = [False] * 101 # 방문 표시

ladder = dict()
snake = dict()
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

q = deque([1])
while q:
    x = q.popleft()
    if x == 100:
        print(board[x]) # 주사위 굴린 횟수
        break # 반복문 탈출
    for dice in range(1, 7):
        next_place = x + dice
        if next_place <= 100 and not visited[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            if next_place in snake.keys():
                next_place = snake[next_place]
            if not visited[next_place]:
                visited[next_place] = True # 방문 표시
                board[next_place] = board[x] + 1 # 주사위 굴린 횟수 추가
                q.append(next_place) # 큐에 이동한 위치 삽입
