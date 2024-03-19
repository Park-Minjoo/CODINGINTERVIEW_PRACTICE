import sys
input = sys.stdin.readline
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    arr = list(map(int, input().split())) # 여러개를 입력받아야 함.
    for s in range(1, arr[0]): # 하나하나 저장
        graph[arr[s]].append(arr[s+1])
        indegree[arr[s+1]] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) != v: print(0)
    else:
        for i in result:
            print(i)

topology_sort()

'''
Input
6 3
3 1 4 3
4 6 2 5 4
2 2 3

Output
6
2
1
5
4
3
'''