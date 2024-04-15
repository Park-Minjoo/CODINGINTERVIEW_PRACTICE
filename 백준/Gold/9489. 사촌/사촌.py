import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    arr = [-1] + list(map(int, input().split()))
    parent = [0] * (n+1)
    parent[0] = -1 # idx를 담은 리스트
    target = 0
    idx = -1
    for i in range(1, n+1):
        if arr[i] == k: # k인 경우
            target = i # i의 인덱스 번호
        if arr[i] != arr[i-1] + 1: # 연속된 숫자가 아닌 경우
            idx += 1 # idx를 증가
        parent[i] = idx
    answer = 0
    for i in range(1, n+1): # 같은 부모안에 있지 않고, 두 부모가 형제인 경우
        if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
            answer += 1
    print(answer)