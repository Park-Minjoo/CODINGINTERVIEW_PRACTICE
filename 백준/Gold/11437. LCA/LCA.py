import sys
sys.setrecursionlimit(int(100000))
input = sys.stdin.readline

n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
visited = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for i in range(n+1)] # graph 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# root node 부터 시작하여 depth를 구하는 함수
def dfs(x, depth):
    visited[x] = True
    d[x] = depth
    for node in graph[x]:
        if visited[node]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[node] = x
        dfs(node, depth + 1)

# A, B의 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
