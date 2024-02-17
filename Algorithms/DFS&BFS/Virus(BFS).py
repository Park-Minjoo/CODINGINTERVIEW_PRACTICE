from collections import deque

n = int(input()) # 컴퓨터 개수
v = int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화, n+1만큼 빈 리스트 생성 (1번 컴퓨터: 1번 인덱스)
visited = [0] * (n+1) # 방문한 노드인가? (0: 미방문, 1:방문)
for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b] # a에 b 연결
    graph[b] += [a] # b에 a 연결
print(graph)
visited[1] = 1 # 첫 번째 컴퓨터
Q = deque([1]) # 첫 번째 컴퓨터에 대한 덱

while Q: # Q에 값이 있는 동안
    print(Q)
    c = Q.popleft() # Q에서 맨 왼쪽에 있는 값이 들어감.
    # print(c, Q)
    for nx in graph[c]: # c번째 컴퓨터와 연결된 리스를 nx로 반복
        if visited[nx] == 0: # nx가 방문하지 않은 컴퓨터
            Q.append(nx) # Q에 추가
            visited[nx] = 1 # 방문 표시
print(sum(visited)-1) # 1번 컴퓨터를 제외하고 출력