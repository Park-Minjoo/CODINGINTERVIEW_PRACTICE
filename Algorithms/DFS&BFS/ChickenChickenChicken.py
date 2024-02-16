import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_cost = 0

for a, b, c in combinations(range(m), 3): #012 013 014 123 124 234
    temp_cost = 0
    for i in range(n): # 3
        temp_cost += max(arr[i][a], arr[i][b], arr[i][c]) #00, 01, 02 -> 11, 12, 13 ...
    max_cost = max(max_cost, temp_cost)
print(max_cost)