import sys
input = sys.stdin.readline

t = int(input())
li = list(map(int, input().split()))

res = [0] * t
for i in range(len(li) - 1):
    if li[i+1] < li[i]:
        res[i]=1

prefix_sum = [0] * (t+1)
for i in range(1, t+1):
    prefix_sum[i] = prefix_sum[i-1] + res[i-1]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(prefix_sum[j-1] - prefix_sum[i-1])