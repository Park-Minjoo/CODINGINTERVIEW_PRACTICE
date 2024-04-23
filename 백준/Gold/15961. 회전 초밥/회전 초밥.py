import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
left, right = 0, k-1

dict = defaultdict(int)
dict[c] = 1 # 쿠폰 번호는 항상 포함되어 있다고 가정

for i in range(k):
    dict[arr[i]] += 1 # 제일 처음 k만큼 dict 추가

result = -int(1e9) # 최대값을 찾기 위해 정의

while left < n:
    result = max(len(dict), result)
    # 슬라이딩
    dict[arr[left]] -= 1 # 제일 왼쪽 스시를 뺌
    if dict[arr[left]] == 0: # 값이 없으면
        del dict[arr[left]] # dict에서 제거
    left += 1
    right += 1
    dict[arr[right % n]] += 1 # 회전초밥이므로 범위를 넘어갈 경우 처음으로 돌아오도록

print(result)