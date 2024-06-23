import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))
visit = set()

queue = deque()

for i in n_list:
    queue.append((i, 1))
    visit.add(i)

result = 0
now_build = 0

while queue:
    now, b = queue.popleft()
    for d in [1, -1]:
        nx = now + d
        if nx in visit:
            continue
        visit.add(nx)
        result += b
        now_build += 1
        queue.append((nx, b+1))
        if now_build == k:
            queue = list()
            break
print(result)